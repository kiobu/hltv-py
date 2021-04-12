from typing import Any

from api.player.request import PlayerRequest
from libs.helper import get_head_data
import libs.logger


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
                    if tag.has_attr('class') and 'playerBodyshot' in tag['class']:
                        img = tag.select("img", attrs={"class": "bodyshot-img"})
                        self.results['image'] = img[0]['src']
        except KeyError as e:
            libs.logger.error(f"There was an issue parsing the body of the page: {repr(e)}")

