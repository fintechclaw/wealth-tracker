from __future__ import annotations

import os
from pathlib import Path
from typing import Dict, Optional


CONFIG_DIR = Path.home() / ".search"
CONFIG_FILE = CONFIG_DIR / "config.toml"


def _parse_toml_kv(content: str) -> Dict[str, str]:
    data: Dict[str, str] = {}
    for raw_line in content.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        data[key] = value
    return data


def load_config(config_file: Optional[Path] = None) -> Dict[str, str]:
    path = config_file or CONFIG_FILE
    if not path.exists():
        return {}
    content = path.read_text(encoding="utf-8")
    return _parse_toml_kv(content)


def save_config(values: Dict[str, str], config_file: Optional[Path] = None) -> Path:
    path = config_file or CONFIG_FILE
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [f'{k} = "{v}"' for k, v in values.items()]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def get_token(config_file: Optional[Path] = None) -> Optional[str]:
    if os.getenv("SEARCH_TOKEN"):
        return os.getenv("SEARCH_TOKEN")
    token = load_config(config_file).get("token")
    return token.strip() if token else None


def set_token(token: str, config_file: Optional[Path] = None) -> Path:
    cleaned = (token or "").strip()
    if not cleaned:
        raise ValueError("token 不能为空")
    current = load_config(config_file)
    current["token"] = cleaned
    return save_config(current, config_file)


def get_base_url() -> str:
    return (os.getenv("SEARCH_BASE_URL") or "http://127.0.0.1:37880").rstrip("/")

