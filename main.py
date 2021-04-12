from typing import Tuple

from models.player.lib import Player
from models.hltv.lib import HLTV

results: Tuple[Player] = HLTV.find_player("Twistzz")

for player in results:
    print(player.player_id)