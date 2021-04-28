from typing import Any
import requests
import hltv.libs.logger

from hltv.api.parser import ResponseParser
from hltv.api.models import Consts


class Request:
    def __init__(self):
        self.url = Consts.HLTV_URL

    def __call__(self):
        hltv.libs.logger.request(f"GET: [{self.url}]")
        parser = ResponseParser(requests.get(self.url, headers={'User-Agent': Consts.USER_AGENT}))
        self.parsed_body: Any = parser()
        return self.parsed_body
