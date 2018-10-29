import pytest

import requests
from json_payload_validator import validate
import logging
import json
from utils import req,request

logging.basicConfig(level=logging.DEBUG)


j_site = 'https://jsonplaceholder.typicode.com'

def test_todos_get():
    schema = {
        "type": "array",
        "properties": {
            "userId": {"type": "integer","minimum":1},
            "id": {"type": "integer","minimum":1,"uniqueItems": True},
            "title": {"type": "string"},
            "completed": {"type": "boolean"}
        }
    }
    r = requests.get(j_site+"/todos")
    error = validate(r.json(), schema)
    assert error == None
    assert r.status_code == 200

def test_todos_last_get():
    url = j_site+"/todos/"
    l = req.json_lenght(url)
    r = requests.get(url+str(l))
    schema = {
        "type": "object",
        "properties": {
            "userId": {"type": "integer"},
            "id": {"type": "integer","value":l},
            "title": {"type": "string"},
            "completed": {"type": "boolean"}
        }
    }
    error = validate(r.json(), schema)
    assert error == None
    assert r.status_code == 200

def test_todos_users_get():
    url = j_site+"/users/"
    l = req.json_lenght(url)
    payload = {"userId":l}
    r = requests.get(j_site+"/todos", params=payload)
    schema = {
        "type": "array",
        "properties": {
            "userId": {"type": "integer","value":l},
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "completed": {"type": "boolean"}
        }
    }
    error = validate(r.json(), schema)
    assert error == None
    assert r.status_code == 200

def test_todos_post():
    url = j_site+"/users/"
    l = req.json_lenght(url)
    url = j_site+"/todos/"
    tod = req.json_lenght(url)
    r = requests.post(j_site+"/todos",data={"title":"post_19:55","completed":False,"userId":l})
    schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "string"},
        "id": {"type": "integer", "value":tod+1},
        "title": {"type": "string","value":"post_19:55"},
        "completed": {"type": "string"}
        }
    }
    error = validate(r.json(), schema)
    assert error == None
    assert r.status_code == 201

def test_todos_put():
    url = j_site+"/users/"
    l = req.json_lenght(url)
    url = j_site+"/todos/"
    tod = req.json_lenght(url)
    r = requests.put(j_site+"/todos/"+str(tod),data={"title":"post_19:55","completed":False,"userId":l,"id":tod})
    schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "string"},
        "id": {"type": "integer", "value":tod},
        "title": {"type": "string","value":"post_19:55"},
        "completed": {"type": "string"}
        }
    }
    error = validate(r.json(), schema)
    assert error == None
    assert r.status_code == 200

def test_todos_patch():
    url = j_site+"/todos/"
    data_name = "title"
    schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string","value":"post_19:55"},
        "completed": {"type": "boolean"}
        }
    }
    assert request.patch_scheme(url,data_name,schema) == None
    assert request.patch_code(url,data_name) == 200

def test_todos_delete():
    url = j_site+"/todos/"
    assert request.delete(url) == 200