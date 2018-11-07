import pytest

import json
import random
import logging
import requests
from json_payload_validator import validate
from utils import req,request
import globals as gbl

logging.basicConfig(level=logging.DEBUG)


def test_posts_get():
    # Тест валидирует json схему запроса постов и код ответа.
    q = request(gbl.posts_url,gbl.schema_posts_get)
    q.get_simple()

@pytest.fixture(scope="function", params=[1,random.randint(2,99),100])
def param_posts(request):
    return request.param

def test_posts_element_get(param_posts):
    # Тест свойств элементов поста. Проверяем граничные значения и 1 случайное.
    url = gbl.posts_url+str(param_posts)
    q = request(url,gbl.schema_posts_element_get)
    q.get_element('id',param_posts)

def test_posts_comm_get(param_posts):
    # get запрос постов, группировка postId, 2 способа запроса одного контента.
    url1 = gbl.posts_url+str(param_posts)+"/comments"
    q = request(url1,gbl.schema_posts_comments_get(param_posts))
    url2 = gbl.comments_url
    payload = {"postId":param_posts}
    q1 = request(url2,gbl.schema_posts_comments_get(param_posts),
                        payload)
    q.get_simple()
    q1.get_payload()

@pytest.fixture(scope="function", params=[1,random.randint(2,9),10])
def param_users(request):
    return request.param

def test_posts_user_get(param_users):
    # get запрос постов, группировка по UserId
    url = gbl.posts_url
    payload = {"userId":param_users}
    q = request(url,gbl.schema_posts_user_get(param_users),payload)
    q.get_payload()

def test_posts_post(param_users):
    # post запрос на добавление нового поста, проверяем при разных userId
    k = req(gbl.posts_url)
    le = k.json_lenght()+1
    payload = {"title":"post_19:55","body":"this is simple new post by me",
               "userId":param_users}
    q = request(gbl.posts_url,gbl.schema_posts_post(param_users,le),
                        payload)
    q.post_simple()

def test_posts_put(param_posts,param_users):
    # put запрос, изменяем данные крайних постов и одного случайного.
    url = gbl.posts_url+str(param_posts)
    payload = {"title":"post_19:55","body":"this is simple new post by me",
               "userId":param_users,"id":param_posts}
    q = request(url,gbl.schema_posts_post(param_users,param_posts),
                       payload)
    q.put_simple()

def test_posts_patch(param_posts):
    # patch запрос, изменяем поле title крайних постов и одного случайного.
    url = gbl.posts_url+str(param_posts)
    payload = {"title":"post_19:55"}
    q = request(url,gbl.schema_posts_patch(param_posts),payload)
    q.patch_simple()

def test_posts_delete(param_posts):
    # Удаляем пост, проверяем код ответа
    url = gbl.posts_url+str(param_posts)
    q = request(url,0)
    q.delete_simple()