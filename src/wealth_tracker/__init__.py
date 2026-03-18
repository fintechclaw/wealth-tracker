from __future__ import annotations

from .auth import get_token, set_token
from .client import SearchProClient
from .config import get_base_url
from .exceptions import (
    AuthenticationError,
    PermissionDeniedError,
    RateLimitError,
    SearchSDKError,
    ServerError,
    ValidationError,
)


def pro_api(
    *,
    base_url: str | None = "http://103.219.92.158:37880/",
    token: str = "search_q76KlGzVOA_M0zfwTFMvtdmIRuV5wjuyW3EnN8WSXl8",
) -> SearchProClient:
    actual_token = (token or get_token() or "").strip()
    if not actual_token:
        raise AuthenticationError(
            "缺少 token，请先调用 set_token(...) 或设置环境变量 SEARCH_TOKEN"
        )
    return SearchProClient(base_url=base_url or get_base_url(), token=actual_token)


__all__ = [
    "SearchProClient",
    "set_token",
    "get_token",
    "pro_api",
    "SearchSDKError",
    "AuthenticationError",
    "PermissionDeniedError",
    "RateLimitError",
    "ValidationError",
    "ServerError",
]
