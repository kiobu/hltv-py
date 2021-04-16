from typing import Any

from api.player.request import PlayerRequest
from libs.helper import *
import libs.logger

from models.team.lib import *


class Player:
    def __init__(self, player_id: int):
        self.body: Any = PlayerRequest(player_id)()
        self.results: dict = dict()
        self.player_id = player_id
        self._canonicalize_body(self.body)

    @staticmethod
    def get(player_id: int):
        return Player(player_id)

    def _canonicalize_body(self, body: Any):
        head = get_head_data(body)
        self.results.update(head)

        try:
            for div in self.body.find_all("div", attrs={"class": "playerContainer"}):
                for tag in div.find_all():
                    if tag.has_attr('class') and 'playerNickname' in tag['class']:
                        self.results['nickname'] = tag.text
                    if tag.has_attr('class') and 'playerRealname' in tag['class']:
                        self.results['real_name'] = tag.text
                        for img in tag.find_all("img", attrs={"itemprop": "nationality"}):
                            self.results['nationality'] = img['title']
                    if tag.has_attr('class') and 'playerTeam' in tag['class']:
                        for a in tag.find_all("a"):
                            if "/team/" in a['href']:
                                self.results['team'] = Team.get(get_id_from_link(a['href']))
                        try:  # Try to access the player's team, and if it KeyErrors, return as None.
                            self.results['team']
                        except KeyError:
                            self.results['team'] = None
                    if tag.has_attr('class') and 'playerBodyshot' in tag['class']:
                        img = tag.select("img", attrs={"class": "bodyshot-img"})
                        self.results['image'] = img[0]['src']
        except KeyError as e:
            libs.logger.error(f"There was an issue parsing the body of the page: {repr(e)}")

