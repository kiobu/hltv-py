import typing
from enum import Enum


class Consts:
    HLTV_URL: str = "https://hltv.org"
    MOCK_UUID: str = "12345678-1234-5678-1234-567812345678"
    USER_AGENT: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                      "Chrome/61.0.3163.79 Safari/537.36 "


class Endpoint(Enum):
    match = "/matches/"
    team = "/team/"
