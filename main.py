from api.match.request import MatchRequest
from match.lib import Match

match_id: int = 2347822

match = Match.get(match_id)

print(match.results['real_link'])