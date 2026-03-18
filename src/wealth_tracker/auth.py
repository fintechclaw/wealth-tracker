from __future__ import annotations

from pathlib import Path
from typing import Optional

from . import config


def set_token(token: str, config_file: Optional[Path] = None) -> Path:
    return config.set_token(token, config_file=config_file)


def get_token(config_file: Optional[Path] = None) -> Optional[str]:
    return config.get_token(config_file=config_file)

