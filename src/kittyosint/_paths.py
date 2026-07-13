"""Path helpers for KittyOSINT."""

from pathlib import Path


def _resolve_framework_root() -> Path:
    try:
        from core.utils.marketplace_apps import framework_root as marketplace_framework_root
    except Exception:
        marketplace_framework_root = None

    if marketplace_framework_root is None:
        return Path(__file__).resolve().parents[2]

    try:
        return Path(marketplace_framework_root()).resolve()
    except Exception:
        return Path(__file__).resolve().parents[2]


def framework_root() -> Path:
    return _resolve_framework_root()


def shared_static_img_dir() -> Path:
    try:
        from core.utils.marketplace_apps import shared_static_img_dir as marketplace_shared_static_dir
    except Exception:
        marketplace_shared_static_dir = None

    if marketplace_shared_static_dir is not None:
        try:
            value = marketplace_shared_static_dir()
            return Path(value).resolve()
        except Exception:
            pass

    return (Path(__file__).resolve().parent / "static").resolve()


__all__ = ["framework_root", "shared_static_img_dir"]
