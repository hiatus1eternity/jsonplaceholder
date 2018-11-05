import pytest

import json
import requests
from json_payload_validator import validate


class req:
    #Вспомогательный класс
    def json_lenght(url):
        # Метод вычисляет количество элементов массива в ответе json
        r=requests.get(url)
        json_data = json.dumps(r.json())
        item_dict = json.loads(json_data)
        le = len(item_dict)
        return le


class request:
    #Класс используется для отправки запросов и валидации ответов
    def get_simple(url,schema):
        # Метод отправляет простой get запрос, валидирует json и код ответа
        r = requests.get(url)
        error = validate(r.json(),schema)
        assert error == None
        assert r.status_code == 200

    def get_element(url,schema,param,value):
        # Метод в дополнение к get запросу валилирует параметр из ответа
        r = requests.get(url)
        error = validate(r.json(),schema)
        assert error == None
        assert r.status_code == 200
        assert r.json()[param] == value

    def get_payload(url,schema,payload):
        # Метод отправляет get запрос с параметрами
        r = requests.get(url,params=payload)
        error = validate(r.json(),schema)
        assert error == None
        assert r.status_code == 200

    def post_simple(url,schema,payload):
        #Метод отправляет post запрос
        r = requests.post(url,data=payload)
        error = validate(r.json(),schema)
        assert error == None
        assert r.status_code == 201

    def put_simple(url,schema,payload):
        r = requests.put(url,data=payload)
        error = validate(r.json(),schema)
        assert error == None
        assert r.status_code == 200

    def patch_simple(url,schema,payload):
        r = requests.patch(url,data=payload)
        error = validate(r.json(),schema)
        assert error == None
        assert r.status_code == 200

    def delete_simple(url):
        r = requests.delete(url)
        assert r.status_code == 200