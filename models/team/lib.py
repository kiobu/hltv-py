from typing import Any

from api.team.request import TeamRequest


class Team:
    def __init__(self, team_id: int):
        self.body: Any = TeamRequest(team_id)()
        self.results: dict = dict()
        self.team_id = team_id

    @staticmethod
    def get(team_id: int):
        return Team(team_id)
