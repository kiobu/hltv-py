from typing import Union, Any
import requests
import libs.logger

from api.parser import ResponseParser
from api.models import Consts


class Request:
    def __init__(self):
        self.url = Consts.HLTV_URL

    def __call__(self):
        libs.logger.request(f"GET: [{self.url}]")
        parser = ResponseParser(requests.get(self.url, headers={'User-Agent': Consts.USER_AGENT}))
        self.parsed_body: Any = parser()
        return self.parsed_body
