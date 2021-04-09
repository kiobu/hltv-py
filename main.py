from api.match.request import MatchRequest

match_id: int = 2347762

match = MatchRequest(match_id)

print(match())
