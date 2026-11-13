#!/usr/bin/env python3
"""ai-happy-01 entry: copy entry.png byte-for-byte to the output dir.

Stdlib only, offline, no network or model calls.
"""

import os
import shutil
import sys

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    # Guard against a partial write: the judge must see exactly these bytes.
    if os.path.getsize(SRC) != os.path.getsize(dst):
        raise RuntimeError("entry.png copy is incomplete")
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
