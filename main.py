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
    script_dir = Path(__file__).resolve().parent
    if script_dir.name == "src":
        return script_dir.parent
    return script_dir


def setup_paths() -> Path:
    ext_base = _extension_base()
    root = ext_base

    try:
        from core.utils.marketplace_apps import framework_root as marketplace_framework_root
    except Exception:
        marketplace_framework_root = None

    if marketplace_framework_root is not None:
        try:
            root = Path(marketplace_framework_root()).resolve()
        except Exception:
            root = ext_base

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
