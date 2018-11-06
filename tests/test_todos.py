import pytest

import json
import random
import logging
import requests
from json_payload_validator import validate
from utils import req,request
import globals as gbl

logging.basicConfig(level=logging.DEBUG)


def test_todos_get():
    # Тест валидирует json схему запроса заданий и код ответа.
    q = request()
    q.get_simple(gbl.todos_url,gbl.schema_todos_get)

@pytest.fixture(scope="function", params=[1,random.randint(2,199),200])
def param_todos(request):
    return request.param

def test_todos_element_get(param_todos):
    # Тест свойств элементов заданий. Проверяем граничные значения и 1 случайное.
    q = request()
    url = gbl.todos_url+str(param_todos)
    q.get_element(url,gbl.schema_todos_element_get,'id',param_todos)

@pytest.fixture(scope="function", params=[1,random.randint(2,9),10])
def param_users(request):
    return request.param

def test_todos_user_get(param_users):
    # get запрос заданий, группировка по UserId
    q = request()
    url = gbl.todos_url
    payload = {"userId":param_users}
    q.get_payload(url,gbl.schema_todos_user_get(param_users),payload)

def test_todos_post(param_users):
    # post запрос на добавление нового задания, проверяем при разных userId
    q = request()
    le = q.json_lenght(gbl.todos_url)+1
    payload = {"title":"post_19:55","completed":False,"userId":param_users}
    q.post_simple(gbl.todos_url,gbl.schema_todos_post(param_users,le),
                        payload)

def test_todos_put(param_todos,param_users):
    # put запрос, изменяем данные крайних заданий и одного случайного.
    q = request()
    url = gbl.todos_url+str(param_todos)
    payload = {"title":"post_19:55","completed":False,"userId":param_users,
              "id":param_todos}
    q.put_simple(url,gbl.schema_todos_post(param_users,param_todos),
                       payload)

def test_todos_patch(param_todos):
    # patch запрос, изменяем поле title крайних заданий и одного случайного.
    q = request()
    url = gbl.todos_url+str(param_todos)
    payload = {"title":"post_19:55"}
    q.patch_simple(url,gbl.schema_todos_patch(param_todos),payload)

def test_todos_delete(param_todos):
    # Удаляем задание, проверяем код ответа
    q = request()
    url = gbl.todos_url+str(param_todos)
    q.delete_simple(url)