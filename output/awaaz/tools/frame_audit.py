#!/usr/bin/env python3
"""Frame-by-frame audit helper for AWAAZ clips and assemblies.

Usage: python3 frame_audit.py VIDEO OUTDIR [--fps 4] [--tile 8x4]

Writes into OUTDIR:
  sheet_NN.png   timestamped contact sheets, `fps` frames per second (default 4)
  report.txt     duration/specs, hard-cut list, speech-activity windows, loudness,
                 and silence gaps, so audio events can be matched to frames
Standard library plus ffmpeg/ffprobe only.
"""
import argparse, math, os, re, struct, subprocess, sys, wave


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video"); ap.add_argument("out")
    ap.add_argument("--fps", type=float, default=4)
    ap.add_argument("--tile", default="8x4")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    cols, rows = [int(x) for x in a.tile.split("x")]
    per = cols * rows
    rep = []

    pr = run(["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=codec_type,width,height,r_frame_rate",
              "-of", "default=nw=1", a.video]).stdout
    rep.append("SPECS\n" + pr)
    dur = float(re.search(r"duration=([\d.]+)", pr).group(1))

    # timestamped sheets (drawtext stamps each frame with its time)
    font = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    vf = (f"fps={a.fps},scale=270:-1,"
          f"drawtext=fontfile={font}:text='%{{pts\\:hms}}':x=6:y=6:fontsize=18:fontcolor=yellow:box=1:boxcolor=black@0.6,"
          f"tile={cols}x{rows}")
    run(["ffmpeg", "-v", "error", "-y", "-i", a.video, "-vf", vf, os.path.join(a.out, "sheet_%02d.png")])

    # hard cuts
    r = run(["ffmpeg", "-hide_banner", "-i", a.video, "-vf", "select='gt(scene,0.3)',showinfo", "-f", "null", "-"]).stderr
    cuts = [float(x) for x in re.findall(r"pts_time:([\d.]+)", r)]
    rep.append("HARD CUTS (scene score > 0.3), seconds\n" + (", ".join(f"{c:.2f}" for c in cuts) or "none"))

    # audio activity
    wav = os.path.join(a.out, "a.wav")
    run(["ffmpeg", "-v", "error", "-y", "-i", a.video, "-vn", "-ac", "1", "-ar", "16000", wav])
    try:
        w = wave.open(wav); n = w.getnframes(); d = struct.unpack("<%dh" % n, w.readframes(n))
    except Exception as e:
        rep.append(f"AUDIO: unreadable ({e})"); d = []
    if d:
        step = 1600  # 0.1 s
        db = []
        for i in range(0, len(d) - step, step):
            r_ = math.sqrt(sum(x * x for x in d[i:i + step]) / step) / 32768
            db.append(20 * math.log10(r_) if r_ > 0 else -99)
        thr = -32
        segs, s = [], None
        for i, v in enumerate(db):
            if v > thr and s is None: s = i
            if v <= thr and s is not None:
                if i - s >= 3: segs.append((s / 10, i / 10))
                s = None
        if s is not None: segs.append((s / 10, len(db) / 10))
        rep.append("SPEECH-LIKE ACTIVITY WINDOWS (level above -32 dB for 0.3 s or more), seconds\n" +
                   ("\n".join(f"  {x:6.1f} to {y:6.1f}" for x, y in segs) or "  none"))
        quiet = [i / 10 for i, v in enumerate(db) if v < -55]
        rep.append(f"DIGITAL-SILENCE SHARE (below -55 dB): {100 * len(quiet) / max(1, len(db)):.0f} percent of the track")
    l = run(["ffmpeg", "-hide_banner", "-i", a.video, "-af", "loudnorm=print_format=summary", "-vn", "-f", "null", "-"]).stderr
    m = re.search(r"Input Integrated:\s+([-\d.]+)", l)
    if m: rep.append(f"INTEGRATED LOUDNESS: {m.group(1)} LUFS")
    rep.append(f"DURATION: {dur:.2f} s. Sheets: {math.ceil(dur * a.fps / per)} at {a.fps} fps.")
    open(os.path.join(a.out, "report.txt"), "w").write("\n\n".join(rep) + "\n")
    print("\n\n".join(rep))


if __name__ == "__main__":
    sys.exit(main())
