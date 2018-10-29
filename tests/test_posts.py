import pytest

import requests
from json_payload_validator import validate
import logging
import json
from utils import req,request

logging.basicConfig(level=logging.DEBUG)


j_site = 'https://jsonplaceholder.typicode.com'

def test_posts_get():
    schema = {
        "type": "array",
        "properties": {
            "userId": {"type": "integer","minimum":1},
            "id": {"type": "integer","minimum":1,"uniqueItems": True},
            "title": {"type": "string"},
            "body": {"type": "string"}
        }
    }
    r = requests.get(j_site+"/posts")
    error = validate(r.json(), schema)
    assert error == None
    assert r.status_code == 200

def test_posts_last_get():
    url = j_site+"/posts/"
    l = req.json_lenght(url)
    r = requests.get(url+str(l))
    schema = {
        "type": "object",
        "properties": {
            "userId": {"type": "integer"},
            "id": {"type": "integer","value":l},
            "title": {"type": "string"},
            "body": {"type": "string"}
        }
    }
    error = validate(r.json(), schema)
    assert error == None
    assert r.status_code == 200

def test_posts_comm_get():
    url = j_site+"/posts/"
    l = req.json_lenght(url)
    r = requests.get(url+str(l)+"/comments")
    payload = {"postId":l}
    r1 = requests.get(j_site+"/comments", params=payload)
    schema = {
        "type": "array",
        "properties": {
            "postId":{"type":"integer","value":l},
            "name":{"type": "string"},
            "id": {"type": "integer","minimum":1,"uniqueItems": True},
            "title": {"type": "string"},
            "body": {"type": "string"}
        }
    }
    error = validate(r.json(), schema)
    assert r.json() == r1.json()
    assert error == None
    assert r.status_code == 200

def test_posts_user_get():
    url = j_site+"/users/"
    l = req.json_lenght(url)
    payload = {"userId":l}
    r = requests.get(j_site+"/posts", params=payload)
    schema = {
        "type": "array",
        "properties": {
            "userId":{"type":"integer","value":l},
            "id": {"type": "integer","minimum":1,"uniqueItems": True},
            "title": {"type": "string"},
            "body": {"type": "string"}
        }
    }
    error = validate(r.json(), schema)
    assert error == None
    assert r.status_code == 200

def test_posts_post():
    userId = 10
    r = requests.post(j_site+"/posts",data={"title":"post_19:55","body":"this is simple new post by me","userId":userId})
    schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "string","value":userId},
        "id": {"type": "integer", "value":101},
        "title": {"type": "string","value":"post_19:55"},
        "body": {"type": "string","value":"this is simple new post by me"}
        }
    }
    error = validate(r.json(), schema)
    assert error == None
    assert r.status_code == 201

def test_posts_put():
    userId = 10
    id = 100
    r = requests.put(j_site+"/posts/"+str(id),data={"title":"post_19:55","body":"this is simple new post by me","userId":userId,"id":id})
    schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "string","value":userId},
        "id": {"type": "integer", "value":100},
        "title": {"type": "string","value":"post_19:55"},
        "body": {"type": "string","value":"this is simple new post by me"}
        }
    }
    error = validate(r.json(), schema)
    assert error == None
    assert r.status_code == 200

def test_posts_patch():
    url = j_site+"/posts/"
    data_name = "title"
    schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string","value":"post_19:55"},
        "body": {"type": "string"}
        }
    }
    assert request.patch_scheme(url,data_name,schema) == None
    assert request.patch_code(url,data_name) == 200

def test_posts_delete():
    url = j_site+"/posts/"
    assert request.delete(url) == 200


