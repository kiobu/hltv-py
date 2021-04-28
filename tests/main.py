import hltv

results = hltv.HLTV.find_player("pikatwist")

for player in results:
    print(str(player.results))
