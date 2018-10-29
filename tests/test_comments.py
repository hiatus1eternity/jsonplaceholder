import pytest

import requests
from json_payload_validator import validate
import logging
import json
from utils import req
logging.basicConfig(level=logging.DEBUG)

j_site = 'https://jsonplaceholder.typicode.com'

def test_comments_get():
    schema = {
        "type": "array",
        "properties": {
            "postId": {"type": "integer","minimum":1},
            "id": {"type": "integer","minimum":1,"uniqueItems": True},
            "name":{"type":"string"},
            "email": {"type": "string","format":"email"},
            "body": {"type": "string"}
        }
    }
    r = requests.get(j_site+"/comments")
    error = validate(r.json(), schema)
    assert error == None
    assert r.status_code == 200

def test_comments_last_get():
    url = j_site+"/comments/"
    l = req.json_lenght(url)
    url = url+str(l)
    r = requests.get(url)
    schema = {
        "type": "object",
        "properties": {
            "postId": {"type": "integer"},
            "id": {"type": "integer","value":l},
            "name":{"type":"string"},
            "email": {"type": "string","format":"email"},
            "body": {"type": "string"}
        }
    }
    error = validate(r.json(), schema)
    assert error == None
    assert r.status_code == 200

def test_comments_postId_get():
    url = j_site+"/posts/"
    l = req.json_lenght(url)
    payload = {"postId":l}
    r = requests.get(j_site+"/comments", params=payload)
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
    assert error == None
    assert r.status_code == 200

def test_comments_post():
    url = j_site+"/posts/"
    postId = req.json_lenght(url)
    url = j_site+"/comments/"
    l = req.json_lenght(url)
    r = requests.post(j_site+"/comments",data={"name":"comm_19:55","body":"this is simple new post by me","postId":postId,"email":"my@my.my"})
    schema = {
    "type": "object",
    "properties": {
        "postId": {"type": "string","value":postId},
        "id": {"type": "integer", "value":l+1},
        "name": {"type": "string","value":"post_19:55"},
        "body": {"type": "string","value":"this is simple new post by me"},
        "email": {"type": "string", "format": "email","value":"my@my.my"}
        }
    }
    error = validate(r.json(), schema)
    assert error == None
    assert r.status_code == 201

def test_comments_put():
    url = j_site+"/comments/"
    l = req.json_lenght(url)
    r = requests.put(j_site+"/comments/"+str(l),data={"name":"comm_19:55","body":"this is simple new post by me","postId":5,"email":"my@my.my"})
    schema = {
    "type": "object",
    "properties": {
        "postId": {"type": "string","value":5},
        "id": {"type": "integer", "value":l},
        "name": {"type": "string","value":"post_19:55"},
        "body": {"type": "string","value":"this is simple new post by me"},
        "email": {"type": "string", "format": "email","value":"my@my.my"}
        }
    }
    error = validate(r.json(), schema)
    assert error == None
    assert r.status_code == 200

def test_comments_patch():
    url = j_site+"/comments/"
    l = req.json_lenght(url)
    r = requests.patch(j_site+"/comments/"+str(l),data={"name":"post_19:55"})
    schema = {
    "type": "object",
    "properties": {
        "postId": {"type": "integer"},
        "id": {"type": "integer", "value":l},
        "name": {"type": "string","value":"post_19:55"},
        "body": {"type": "string"},
        "email": {"type": "string", "format": "email"}

    }
    }
    error = validate(r.json(), schema)
    assert error == None
    assert r.status_code == 200

def test_comments_delete():
    url = j_site + "/posts/" + str(100)
    r = requests.delete(url)
    assert r.status_code == 200