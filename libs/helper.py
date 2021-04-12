from typing import Any


def get_head_data(body: Any):
    return {
        "title": body.select("title")[0].text,
        "real_link": body.find_all("link", {"rel": "canonical"})[0]['href']
    }
