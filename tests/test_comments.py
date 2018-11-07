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
    q = request(gbl.comments_url, gbl.scheme_comments_get)
    q.get_simple()

@pytest.fixture(scope="function", params=[1,random.randint(2,499),500])
def param_comments(request):
    return request.param

def test_comments_element_get(param_comments):
    url = gbl.comments_url+str(param_comments)
    q = request(url,gbl.schema_comments_element_get)
    q.get_element('id', param_comments)

@pytest.fixture(scope="function", params=[1,random.randint(2,99),100])
def param_posts(request):
    return request.param

def test_comments_postId_get(param_posts):
    # get запрос комментов, группировка по postId
    url = gbl.comments_url
    payload = {"postId":param_posts}
    q = request(url,gbl.schema_comments_postId_get(param_posts),payload)
    q.get_payload()

def test_comments_post(param_posts):
    # post запрос на добавление нового поста, проверяем при разных userId
    k = req(gbl.comments_url)
    le = k.json_lenght()+1
    payload = {"name":"comm_19:55","body":"this is simple new post by me",
               "postId":param_posts,"email":"my@my.my"}
    q = request(gbl.comments_url,gbl.schema_comments_post(param_posts,le),
                payload)
    q.post_simple()

def test_comments_put(param_comments,param_posts):
    # put запрос, изменяем данные крайних комментов и одного случайного.
    url = gbl.comments_url+str(param_comments)
    payload = {"name":"comm_19:55","body":"this is simple new post by me",
               "postId":param_posts,"email":"my@my.my"}
    q = request(url,gbl.schema_comments_post(param_posts,param_comments),
                payload)
    q.put_simple()

def test_comments_patch(param_comments):
    # patch запрос, изменяем поле name крайних комментов и одного случайного.
    url = gbl.comments_url+str(param_comments)
    payload = {"name":"post_19:55"}
    q = request(url,gbl.schema_comments_patch(param_comments),payload)
    q.patch_simple()

def test_comments_delete(param_comments):
    # Удаляем коммент, проверяем код ответа
    url = gbl.comments_url+str(param_comments)
    q = request(url,0)
    q.delete_simple()