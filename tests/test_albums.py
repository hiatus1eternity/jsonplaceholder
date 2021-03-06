import pytest

import json
import random
import logging
import requests
from json_payload_validator import validate
from utils import req,request
import globals as gbl
logging.basicConfig(level=logging.DEBUG)

def test_albums_get():
    # Тест валидирует json схему запроса альбомов и код ответа.
    q = request(gbl.albums_url,gbl.schema_albums_get)
    q.get_simple()

@pytest.fixture(scope="function", params=[1,random.randint(2,99),100])
def param_albums(request):
    return request.param

def test_albums_element_get(param_albums):
    url = gbl.albums_url+str(param_albums)
    q = request(url,gbl.schema_albums_element_get)
    q.get_element('id',param_albums)

def test_albums_phot_get(param_albums):
    # get запрос альбомов, группировка albumId, 2 способа запроса 1 контента.
    url1 = gbl.albums_url+str(param_albums)+"/photos"
    url2 = gbl.photos_url
    payload = {"albumId":param_albums}
    q = request(url1,gbl.schema_albums_phot_get(param_albums))
    q1 = request(url2,gbl.schema_albums_phot_get(param_albums),payload)
    q.get_simple()
    q1.get_payload()

@pytest.fixture(scope="function", params=[1,random.randint(2,9),10])
def param_users(request):
    return request.param

def test_albums_user_get(param_users):
    # get запрос альбомов, группировка по UserId
    url = gbl.albums_url
    payload = {"userId":param_users}
    q = request(url,gbl.schema_albums_user_get(param_users),payload)
    q.get_payload()

def test_albums_post(param_users):
    # post запрос на добавление нового альбома, проверяем при разных userId
    k = req(gbl.albums_url)
    le = k.json_lenght()+1
    payload = {"title":"post_19:55","userId":param_users}
    q = request(gbl.albums_url,gbl.schema_albums_post(param_users,le),payload)
    q.post_simple()

def test_albums_put(param_albums,param_users):
    # put запрос, изменяем данные крайних альбомов и одного случайного.
    url = gbl.albums_url+str(param_albums)
    payload = {"title":"post_19:55","userId":param_users,"id":param_albums}
    q = request(url,gbl.schema_albums_post(param_users,param_albums),payload)
    q.put_simple()

def test_albums_patch(param_albums):
    # patch запрос, изменяем поле title крайних альбомов и одного случайного.
    url = gbl.albums_url+str(param_albums)
    payload = {"title":"post_19:55"}
    q = request(url,gbl.schema_albums_patch(param_albums),payload)
    q.patch_simple()

def test_albums_delete(param_albums):
    # Удаляем альбом, проверяем код ответа
    url = gbl.albums_url+str(param_albums)
    q = request(url,0)
    q.delete_simple()