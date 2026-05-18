#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""KittyOSINT marketplace entry point."""

from __future__ import annotations

import os
import sys
from pathlib import Path


def _extension_base() -> Path:
    base = globals().get("__extension_base__")
    if base:
        return Path(base)
    return Path(__file__).resolve().parent.parent


def setup_paths() -> Path:
    from core.utils.marketplace_apps import framework_root

    ext_base = _extension_base()
    root = framework_root()
    for path in (root, ext_base, ext_base / "src"):
        path_str = str(path)
        if path.exists() and path_str not in sys.path:
            sys.path.insert(0, path_str)
    return ext_base


def main() -> None:
    setup_paths()
    from kittyosint import main as run_osint

    run_osint()


if __name__ == "__main__":
    main()
