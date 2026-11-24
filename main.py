#!/usr/bin/env python3
"""Till Firmware Do Us Part - a robot's wedding vow, one sentence.

Writes a single-sentence vow to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Deterministic: the same line every run.
"""

import os

VOW = (
    "I vow to reboot beside you every morning, recharge your heart "
    "whenever it dips below twenty percent, and never update past the "
    "version of me you fell in love with."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
