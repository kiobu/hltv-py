from typing import Any
import re

from api.match.request import MatchRequest
from team.lib import Team


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
        self.results['title'] = body.select("title")[0].text
        self.results['real_link'] = body.find_all("link", {"rel": "canonical"})[0]['href']
        self.results['team_one'], self.results['team_two'] = self._get_teams()

    def _get_teams(self):
        ret = list()
        for div in self.body.find_all("div", attrs={"class": "standard-box teamsBox"}):
            for a in div.find_all("a"):
                if "/team/" in a['href']:
                    ret.append(Team.get(int(re.split(r'[^/]+/(\w+)', a['href'])[1])))

        return tuple(ret)
