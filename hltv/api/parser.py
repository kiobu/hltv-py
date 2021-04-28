from typing import Any

from requests import Response
from bs4 import BeautifulSoup


class ResponseParser:
    def __init__(self, response: Response):
        self.parsed: Any = BeautifulSoup(response.content, 'html.parser')

    def __call__(self):
        return self.parsed
