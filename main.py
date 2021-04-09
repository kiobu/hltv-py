from api.base_request import Request
from api.models import Endpoint

# tests
req = Request()
print(req().select_one("a"))
