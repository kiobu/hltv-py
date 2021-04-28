from hltv.api.base_request import Request
from hltv.api.models import Endpoint, Consts


class PlayerRequest(Request):
    def __init__(self, player_id: int):
        super().__init__()
        self.player_id = player_id

        self.url += Endpoint.player.value + str(self.player_id)  # Set request URL to include the match ID.
        self._attach_uuid()

    def _attach_uuid(self):
        self.url += f"/{Consts.MOCK_UUID}"

    def __call__(self):
        return super().__call__()
