from typing import Tuple

from models.player.lib import Player
from models.hltv.lib import HLTV
import libs.logger

results: Tuple[Player] = HLTV.find_player("n0thing")

for player in results:
    print(str(player.results))
