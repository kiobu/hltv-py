from typing import Union, Any
import requests

from api.parser import ResponseParser
from api.consts import Consts


class Request:
    def __init__(self):
        self.url = Consts.HLTV_URL

    def __call__(self):
        parser = ResponseParser(requests.get(self.url))
        self.parsed_body: Any = parser()
        return self.parsed_body
