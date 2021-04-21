import re

from typing import Union, Type, Any

from api.hltv.search_request import SearchRequest
from models.player.lib import Player
from models.team.lib import Team


class HLTV:
    def __init__(self):
        pass

    @staticmethod
    def _find(class_kind: Union[Type[Player], Type[Team]], query: str):  # Types in Union must be ID-indexed (ints).
        query = query.replace(" ", "+")
        response_body = SearchRequest(query)()
        return HLTV._get_results(response_body, class_kind)

    @staticmethod
    def _get_results(body: Any, class_kind):
        ret = list()
        for div in body.find_all("div", attrs={"class": "contentCol"}):
            for a in div.find_all("a"):
                if f"/{class_kind.__name__.lower()}/" in a['href']:
                    ret.append(class_kind(int(re.split(r'[^/]+/(\w+)', a['href'])[1])))

        return tuple(ret)

    @staticmethod
    def find_player(query: str):
        return HLTV._find(Player, query)

    @staticmethod
    def find_team(query: str):
        return HLTV._find(Team, query)
