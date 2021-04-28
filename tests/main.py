from package import *

results = HLTV.find_player("n0thing")

for player in results:
    print(str(player.results))
