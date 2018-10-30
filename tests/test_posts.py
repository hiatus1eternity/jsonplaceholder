import pytest

import requests
from json_payload_validator import validate
import logging
import json
from utils import req,request
import globals as gbl

logging.basicConfig(level=logging.DEBUG)


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
    url = gbl.j_site+"/posts"
    gt = request.get_scheme(url,schema)
    assert gt[0] == None
    assert gt[1] == 200

def test_posts_last_get():
    url = gbl.j_site+"/posts/"
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
    url = gbl.j_site+"/posts/"
    l = req.json_lenght(url)
    r = requests.get(url+str(l)+"/comments")
    payload = {"postId":l}
    r1 = requests.get(gbl.j_site+"/comments", params=payload)
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
    url = gbl.j_site+"/users/"
    l = req.json_lenght(url)
    payload = {"userId":l}
    r = requests.get(gbl.j_site+"/posts", params=payload)
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
    r = requests.post(gbl.j_site+"/posts",data={"title":"post_19:55","body":"this is simple new post by me","userId":userId})
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
    r = requests.put(gbl.j_site+"/posts/"+str(id),data={"title":"post_19:55","body":"this is simple new post by me","userId":userId,"id":id})
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
    url = gbl.j_site+"/posts/"
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
    pt = request.patch_scheme(url,data_name,schema)
    assert pt[0] == None
    assert pt[1] == 200

def test_posts_delete():
    url = gbl.j_site+"/posts/"
    assert request.delete(url) == 200


