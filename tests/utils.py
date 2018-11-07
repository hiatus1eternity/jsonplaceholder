import pytest

import json
import requests
from json_payload_validator import validate


class req:
    #Вспомогательный класс

    def __init__(self,url):
        self.url = url

    def json_lenght(self):
        # Метод вычисляет количество элементов массива в ответе json
        r = requests.get(self.url)
        json_data = json.dumps(r.json())
        item_dict = json.loads(json_data)
        le = len(item_dict)
        return le


class request(req):
    #Класс используется для отправки запросов и валидации ответов

    def __init__(self,url,schema,payload=0):
        self.url = url
        self.schema = schema
        self.payload = payload

    def get_simple(self):
        # Метод отправляет простой get запрос, валидирует json и код ответа
        r = requests.get(self.url)
        error = validate(r.json(),self.schema)
        assert error == None
        assert r.status_code == 200

    def get_element(self,param,value):
        # Метод в дополнение к get запросу валилирует параметр из ответа
        r = requests.get(self.url)
        error = validate(r.json(),self.schema)
        assert error == None
        assert r.status_code == 200
        assert r.json()[param] == value

    def get_payload(self):
        # Метод отправляет get запрос с параметрами
        r = requests.get(self.url,params=self.payload)
        error = validate(r.json(),self.schema)
        assert error == None
        assert r.status_code == 200

    def post_simple(self):
        #Метод отправляет post запрос
        r = requests.post(self.url,data=self.payload)
        error = validate(r.json(),self.schema)
        assert error == None
        assert r.status_code == 201

    def put_simple(self):
        r = requests.put(self.url,data=self.payload)
        error = validate(r.json(),self.schema)
        assert error == None
        assert r.status_code == 200

    def patch_simple(self):
        r = requests.patch(self.url,data=self.payload)
        error = validate(r.json(),self.schema)
        assert error == None
        assert r.status_code == 200

    def delete_simple(self):
        r = requests.delete(self.url)
        assert r.status_code == 200