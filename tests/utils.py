import pytest

import json
import requests
from json_payload_validator import validate


class req:
    #Вспомогательный класс
    def json_lenght(self,url):
        # Метод вычисляет количество элементов массива в ответе json
        self.r = requests.get(url)
        self.json_data = json.dumps(self.r.json())
        self.item_dict = json.loads(self.json_data)
        self.le = len(self.item_dict)
        return self.le


class request(req):
    #Класс используется для отправки запросов и валидации ответов
    def get_simple(self,url,schema):
        # Метод отправляет простой get запрос, валидирует json и код ответа
        self.r = requests.get(url)
        self.error = validate(self.r.json(),schema)
        assert self.error == None
        assert self.r.status_code == 200

    def get_element(self,url,schema,param,value):
        # Метод в дополнение к get запросу валилирует параметр из ответа
        self.r = requests.get(url)
        self.error = validate(self.r.json(),schema)
        assert self.error == None
        assert self.r.status_code == 200
        assert self.r.json()[param] == value

    def get_payload(self,url,schema,payload):
        # Метод отправляет get запрос с параметрами
        self.r = requests.get(url,params=payload)
        self.error = validate(self.r.json(),schema)
        assert self.error == None
        assert self.r.status_code == 200

    def post_simple(self,url,schema,payload):
        #Метод отправляет post запрос
        self.r = requests.post(url,data=payload)
        self.error = validate(self.r.json(),schema)
        assert self.error == None
        assert self.r.status_code == 201

    def put_simple(self,url,schema,payload):
        self.r = requests.put(url,data=payload)
        self.error = validate(self.r.json(),schema)
        assert self.error == None
        assert self.r.status_code == 200

    def patch_simple(self,url,schema,payload):
        self.r = requests.patch(url,data=payload)
        self.error = validate(self.r.json(),schema)
        assert self.error == None
        assert self.r.status_code == 200

    def delete_simple(self,url):
        self.r = requests.delete(url)
        assert self.r.status_code == 200