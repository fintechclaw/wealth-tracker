class SearchSDKError(Exception):
    """Base exception for wealth_tracker."""


class AuthenticationError(SearchSDKError):
    """Raised when token is missing or invalid."""


class PermissionDeniedError(SearchSDKError):
    """Raised when caller has no permission."""


class RateLimitError(SearchSDKError):
    """Raised when request rate or quota is exceeded."""


class ValidationError(SearchSDKError):
    """Raised on invalid request payload."""


class ServerError(SearchSDKError):
    """Raised when server returns 5xx."""
