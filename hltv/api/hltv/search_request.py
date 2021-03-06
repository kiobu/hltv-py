from hltv.api.base_request import Request
from hltv.api.models import Endpoint


class SearchRequest(Request):
    def __init__(self, query: str):
        super().__init__()
        self.search_query = query

        self.url += Endpoint.search.value + str(self.search_query)  # Set request URL to include the match ID

    def __call__(self):
        return super().__call__()
