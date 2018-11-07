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
    q = request(gbl.todos_url,gbl.schema_todos_get)
    q.get_simple()

@pytest.fixture(scope="function", params=[1,random.randint(2,199),200])
def param_todos(request):
    return request.param

def test_todos_element_get(param_todos):
    # Тест свойств элементов заданий. Проверяем граничные значения и 1 случайное.
    url = gbl.todos_url+str(param_todos)
    q = request(url,gbl.schema_todos_element_get)
    q.get_element('id',param_todos)

@pytest.fixture(scope="function", params=[1,random.randint(2,9),10])
def param_users(request):
    return request.param

def test_todos_user_get(param_users):
    # get запрос заданий, группировка по UserId
    url = gbl.todos_url
    payload = {"userId":param_users}
    q = request(url,gbl.schema_todos_user_get(param_users),payload)
    q.get_payload()

def test_todos_post(param_users):
    # post запрос на добавление нового задания, проверяем при разных userId
    k = req(gbl.todos_url)
    le = k.json_lenght()+1
    payload = {"title":"post_19:55","completed":False,"userId":param_users}
    q = request(gbl.todos_url,gbl.schema_todos_post(param_users,le),
                payload)
    q.post_simple()

def test_todos_put(param_todos,param_users):
    # put запрос, изменяем данные крайних заданий и одного случайного.
    url = gbl.todos_url+str(param_todos)
    payload = {"title":"post_19:55","completed":False,"userId":param_users,
              "id":param_todos}
    q = request(url,gbl.schema_todos_post(param_users,param_todos),
                       payload)
    q.put_simple()

def test_todos_patch(param_todos):
    # patch запрос, изменяем поле title крайних заданий и одного случайного.
    url = gbl.todos_url+str(param_todos)
    payload = {"title":"post_19:55"}
    q = request(url,gbl.schema_todos_patch(param_todos),payload)
    q.patch_simple()

def test_todos_delete(param_todos):
    # Удаляем задание, проверяем код ответа
    url = gbl.todos_url+str(param_todos)
    q = request(url,0)
    q.delete_simple()