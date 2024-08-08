from typing import Optional

class APIException(Exception):
    def __init__(self, status_code: int, content: dict[str, str], headers: Optional[dict[str, str]]):
        self.status_code = status_code
        self.content = content
        self.headers = headers
