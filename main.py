from api.match.request import MatchRequest

match_id: int = 2347822

match = MatchRequest(match_id)

print(match.url)
print(match())
