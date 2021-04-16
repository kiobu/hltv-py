from typing import Any
import re

from api.match.request import MatchRequest
from models.team.lib import Team
from libs.helper import *


class Match:
    def __init__(self, match_id: int):
        self.body: Any = MatchRequest(match_id)()
        self.results: dict = dict()
        self.match_id = match_id
        self._canonicalize_body(self.body)

    @staticmethod
    def get(match_id: int):
        return Match(match_id)

    def _canonicalize_body(self, body: Any):
        head = get_head_data(body)
        self.results.update(head)
        self.results['team_one'], self.results['team_two'] = self._get_teams()

    def _get_teams(self):
        ret = list()
        for div in self.body.find_all("div", attrs={"class": "standard-box teamsBox"}):
            for a in div.find_all("a"):
                if "/team/" in a['href']:
                    ret.append(Team.get(get_id_from_link(a['href'])))

        return tuple(ret)
