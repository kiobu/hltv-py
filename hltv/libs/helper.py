from typing import Any


def get_head_data(body: Any):
    return {
        "title": body.select("title")[0].text,
        "real_link": body.find_all("link", {"rel": "canonical"})[0]['href']
    }


def get_id_from_link(src: str):
    import re
    return int(re.split(r'[^/]+/(\w+)', src)[1])
