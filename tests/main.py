import hltv

results = hltv.HLTV.find_player("n0thing")

for player in results:
    print(str(player.results))
