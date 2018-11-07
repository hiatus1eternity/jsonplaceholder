import pytest

import json
import random
import logging
import requests
from json_payload_validator import validate
from utils import req,request
import globals as gbl

logging.basicConfig(level=logging.DEBUG)


def test_users_get():
    # Тест валидирует json схему запроса юзеров и код ответа.
    q = request(gbl.users_url,gbl.schema_users_get)
    q.get_simple()

@pytest.fixture(scope="function", params=[1,random.randint(2,9),10])
def param_users(request):
    return request.param

def test_users_element_get(param_users):
    # Проверяем граничные значения и 1 случайное.
    url = gbl.users_url+str(param_users)
    q = request(url,gbl.schema_users_element_get)
    q.get_element('id',param_users)

def test_users_post():
    # post запрос на добавление нового юзера.
    k = req(gbl.users_url)
    le = k.json_lenght()+1
    payload = {
        "name":"Glenna Reichert",
        "username":"Delphine",
        "email":"Chaim_McDermott@dana.io",
        "address":{
            "street":"Dayna Park",
            "suite":"Suite 449",
            "city":"Bartholomebury",
            "zipcode":"76495-3109",
            "geo":{"lat": "24.6463","lng": "-168.8889"}
            },
        "phone":"(775)976-6794 x41206",
        "website":"conrad.com",
        "company":{
            "name":"Yost and Sons",
            "catchPhrase":"Switchable contextually-based project",
            "bs":"aggregate real-time technologies"
            }
        }
    q = request(gbl.users_url,gbl.schema_users_post(le),payload)
    q.post_simple()

def test_users_put(param_users):
    # Изменяем данные крайних юзеров и одного случайного.
    url = gbl.users_url+str(param_users)
    payload = {
        "id":param_users,
        "name":"Glenna Reichert",
        "username":"Delphine",
        "email":"Chaim_McDermott@dana.io",
        "address":{
            "street":"Dayna Park",
            "suite":"Suite 449",
            "city":"Bartholomebury",
            "zipcode":"76495-3109",
            "geo":{"lat": "24.6463","lng": "-168.8889"}
            },
        "phone":"(775)976-6794 x41206",
        "website":"conrad.com",
        "company":{
            "name":"Yost and Sons",
            "catchPhrase":"Switchable contextually-based project",
            "bs":"aggregate real-time technologies"
            }
        }
    q = request(url,gbl.schema_users_post(param_users),payload)
    q.put_simple()

def test_users_patch(param_users):
    # patch запрос, изменяем поле name крайних юзеров и одного случайного.
    url = gbl.users_url+str(param_users)
    payload = {"name":"post_19:55"}
    q = request(url,gbl.schema_users_patch(param_users),payload)
    q.patch_simple()

def test_users_delete(param_users):
    # Удаляем юзера, проверяем код ответа
    url = gbl.users_url+str(param_users)
    q = request(url,0)
    q.delete_simple()