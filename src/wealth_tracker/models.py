from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class TimeRange:
    start_time: Optional[str] = None
    end_time: Optional[str] = None

