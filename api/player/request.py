from api.base_request import Request
from api.models import Endpoint, Consts


class PlayerRequest(Request):
    def __init__(self, match_id: int):
        super().__init__()
        self.match_id = match_id

        self.url += Endpoint.player.value + str(self.match_id)  # Set request URL to include the match ID.
        self._attach_uuid()

    def _attach_uuid(self):
        self.url += f"/{Consts.MOCK_UUID}"

    def __call__(self):
        return super().__call__()
