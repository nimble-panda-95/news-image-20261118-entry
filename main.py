#!/usr/bin/env python3
"""Entry for make.fun news-image-20261118.

Copies the finished infographic (entry.png, drawn by code from the verified
news of Wednesday 18 November 2026) to the grader's output path. Standard
library only; the run is deterministic, the same bytes every time.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT_DIR.mkdir(parents=True, exist_ok=True)
source = HERE / "entry.png"
if not source.is_file():
    raise SystemExit(f"missing image beside the entrypoint: {source}")
shutil.copyfile(source, OUT_DIR / "entry.png")
print(f"wrote {OUT_DIR / 'entry.png'} ({source.stat().st_size} bytes)")
