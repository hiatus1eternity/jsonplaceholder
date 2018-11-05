import pytest

import json
import random
import logging
import requests
from json_payload_validator import validate
from utils import req,request
import globals as gbl

logging.basicConfig(level=logging.DEBUG)


def test_photos_get():
    # Тест валидирует json схему запроса всех фото и код ответа.
    request.get_simple(gbl.photos_url, gbl.schema_photos_get)

@pytest.fixture(scope="function", params=[1,random.randint(2,4999),5000])
def param_photos(request):
    return request.param

def test_photos_element_get(param_photos):
    # Тест свойств элементов конкретного коммента
    url = gbl.photos_url+str(param_photos)
    request.get_element(url,gbl.schema_photos_element_get,'id',param_photos)

@pytest.fixture(scope="function", params=[1,random.randint(2,99),100])
def param_albums(request):
    return request.param

def test_photos_albumid_get(param_albums):
    # get запрос фото, группировка по albumId
    url = gbl.comments_url
    payload = {"albumId":param_albums}
    request.get_payload(url,gbl.schema_photos_albumid_get(param_albums),
                        payload)

def test_photos_post(param_albums):
    # post запрос на добавление нового фото, проверяем при разных albumId
    le = req.json_lenght(gbl.photos_url)+1
    payload = {"title":"post_19:55","url":"https://azcxards.net/3/1",
              "thumbnailUrl":"https://azcxards.net/3/1","albumId":param_albums}
    request.post_simple(gbl.photos_url,
                        gbl.schema_photos_post(param_albums,le),payload)

def test_photos_put(param_photos,param_albums):
    # put запрос, изменяем данные крайних фото и одного случайного.
    url = gbl.photos_url+str(param_photos)
    payload = {"title":"post_19:55","url":"https://azcxards.net/3/1",
              "thumbnailUrl":"https://azcxards.net/3/1","albumId":param_albums}
    request.put_simple(url,gbl.schema_photos_post(param_albums,
                                                    param_photos),payload)

def test_photos_patch(param_photos):
    # patch запрос, изменяем поле title крайних фото и одного случайного.
    url = gbl.photos_url+str(param_photos)
    payload = {"title":"post_19:55"}
    request.patch_simple(url,gbl.schema_photos_patch(param_photos),payload)

def test_photos_delete(param_photos):
    # Удаляем фото, проверяем код ответа
    url = gbl.photos_url+str(param_photos)
    request.delete_simple(url)
