"""Define custom API exceptions."""

from typing import Optional


class APIError(Exception):
    """Represent an API exception response."""

    def __init__(
        self, status_code: int, content: dict[str, str], headers: Optional[dict[str, str]]
    ):
        """Initialize the exception response data."""
        self.status_code = status_code
        self.content = content
        self.headers = headers
