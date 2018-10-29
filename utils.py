import pytest

import requests
from json_payload_validator import validate
import json


class req:
    def json_lenght(url):
        r=requests.get(url)
        json_data = json.dumps(r.json())
        item_dict = json.loads(json_data)
        l = len(item_dict)
        return l
