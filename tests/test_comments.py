import pytest

import json
import random
import logging
import requests
from json_payload_validator import validate
from utils import req,request
import globals as gbl
logging.basicConfig(level=logging.DEBUG)

def test_comments_get():
    # Тест валидирует json схему запроса всех альбомов и код ответа.
    q = request()
    q.get_simple(gbl.comments_url, gbl.scheme_comments_get)

@pytest.fixture(scope="function", params=[1,random.randint(2,499),500])
def param_comments(request):
    return request.param

def test_comments_element_get(param_comments):
    q = request()
    url = gbl.comments_url+str(param_comments)
    q.get_element(url,gbl.schema_comments_element_get,'id',
                        param_comments)

@pytest.fixture(scope="function", params=[1,random.randint(2,99),100])
def param_posts(request):
    return request.param

def test_comments_postId_get(param_posts):
    # get запрос комментов, группировка по postId
    q = request()
    url = gbl.comments_url
    payload = {"postId":param_posts}
    q.get_payload(url,gbl.schema_comments_postId_get(param_posts),
                        payload)

def test_comments_post(param_posts):
    # post запрос на добавление нового поста, проверяем при разных userId
    q = request()
    le = q.json_lenght(gbl.comments_url)+1
    payload = {"name":"comm_19:55","body":"this is simple new post by me",
               "postId":param_posts,"email":"my@my.my"}
    q.post_simple(gbl.comments_url,
                        gbl.schema_comments_post(param_posts,le),payload)

def test_comments_put(param_comments,param_posts):
    # put запрос, изменяем данные крайних комментов и одного случайного.
    q = request()
    url = gbl.comments_url+str(param_comments)
    payload = {"name":"comm_19:55","body":"this is simple new post by me",
               "postId":param_posts,"email":"my@my.my"}
    q.put_simple(url,gbl.schema_comments_post(param_posts,
                                                    param_comments),payload)

def test_comments_patch(param_comments):
    # patch запрос, изменяем поле name крайних комментов и одного случайного.
    q = request()
    url = gbl.comments_url+str(param_comments)
    payload = {"name":"post_19:55"}
    q.patch_simple(url,gbl.schema_comments_patch(param_comments),payload)

def test_comments_delete(param_comments):
    # Удаляем коммент, проверяем код ответа
    q = request()
    url = gbl.comments_url+str(param_comments)
    q.delete_simple(url)