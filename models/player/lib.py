from typing import Any

from api.player.request import PlayerRequest


class Player:
    def __init__(self, player_id: int):
        self.body: Any = PlayerRequest(player_id)()
        self.results: dict = dict()
        self.player_id = player_id

    @staticmethod
    def get(player_id: int):
        return Player(player_id)
