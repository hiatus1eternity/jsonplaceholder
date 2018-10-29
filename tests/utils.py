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


class request:
    def delete(url):
        alb = req.json_lenght(url)
        url1 = url + str(alb)
        r = requests.delete(url1)
        return r.status_code

    def patch_scheme(url,data_name,schema):
        tod = req.json_lenght(url)
        r = requests.patch(url + str(tod), data={data_name: "post_19:55"})
        error = validate(r.json(), schema)
        return error
    def patch_code(url,data_name):
        tod = req.json_lenght(url)
        r = requests.patch(url + str(tod), data={data_name: "post_19:55"})
        return r.status_code