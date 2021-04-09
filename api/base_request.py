from typing import Union, Any
import requests

from bs4 import BeautifulSoup
from api.parser import ResponseParser
from api.models import *
from api.consts import Consts


class Request:
    def __init__(self, endpoint: Endpoint = None, params: list = None):
        self.url = Consts.HLTV_URL
        self.endpoint = endpoint
        self.params = params

    def __call__(self):
        parser = ResponseParser(requests.get(self.url))
        self.parsed_body: Any = parser()
        return self.parsed_body
