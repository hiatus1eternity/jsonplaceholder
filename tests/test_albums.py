import pytest

import requests
from json_payload_validator import validate
import logging
import json
from utils import req,request
import globals as gbl
logging.basicConfig(level=logging.DEBUG)



def test_albums_get():
    schema = {
        "type": "array",
        "properties": {
            "userId": {"type": "integer","minimum":1},
            "id": {"type": "integer","minimum":1,"uniqueItems": True},
            "title": {"type": "string"}
        }
    }
    url = gbl.j_site+"/albums"
    gt = request.get_scheme(url,schema)
    assert gt[0] == None
    assert gt[1] == 200

def test_albums_last_get():
    url = gbl.j_site+"/albums/"
    l = req.json_lenght(url)
    r = requests.get(url+str(l))
    schema = {
        "type": "object",
        "properties": {
            "userId": {"type": "integer"},
            "id": {"type": "integer","value":l},
            "title": {"type": "string"}
        }
    }
    error = validate(r.json(), schema)
    assert error == None
    assert r.status_code == 200

def test_albums_phot_get():
    url = gbl.j_site+"/albums/"
    l = req.json_lenght(url)
    r = requests.get(url+str(l)+"/photos")
    payload = {"albumId":l}
    r1 = requests.get(gbl.j_site+"/photos", params=payload)
    schema = {
        "type": "array",
        "properties": {
            "albumId":{"type":"integer","value":l},
            "url":{"type": "string"},
            "id": {"type": "integer","minimum":1,"uniqueItems": True},
            "title": {"type": "string"},
            "thumbnailUrl": {"type": "string"}
        }
    }
    error = validate(r.json(), schema)
    assert r.json() == r1.json()
    assert error == None
    assert r.status_code == 200

def test_albums_user_get():
    url = gbl.j_site+"/users/"
    l = req.json_lenght(url)
    payload = {"userId":l}
    r = requests.get(gbl.j_site+"/albums", params=payload)
    schema = {
        "type": "array",
        "properties": {
            "userId":{"type":"integer","value":l},
            "id": {"type": "integer","minimum":1,"uniqueItems": True},
            "title": {"type": "string"}
        }
    }
    error = validate(r.json(), schema)
    assert error == None
    assert r.status_code == 200

def test_albums_post():
    url = gbl.j_site+"/users/"
    l = req.json_lenght(url)
    url = gbl.j_site+"/albums/"
    alb = req.json_lenght(url)
    r = requests.post(gbl.j_site+"/albums",data={"title":"post_19:55","userId":l})
    schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "string","value":l},
        "id": {"type": "integer", "value":alb+1},
        "title": {"type": "string","value":"post_19:55"}
        }
    }
    error = validate(r.json(), schema)
    assert error == None
    assert r.status_code == 201

def test_albums_put():
    url = gbl.j_site+"/users/"
    l = req.json_lenght(url)
    url = gbl.j_site+"/albums/"
    alb = req.json_lenght(url)
    r = requests.put(gbl.j_site+"/albums/"+str(alb),data={"title":"post_19:55","userId":l,"id":alb})
    schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "string","value":l},
        "id": {"type": "integer", "value":alb},
        "title": {"type": "string","value":"post_19:55"}
        }
    }
    error = validate(r.json(), schema)
    assert error == None
    assert r.status_code == 200

def test_albums_patch():
    url = gbl.j_site+"/albums/"
    data_name="title"
    schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string","value":"post_19:55"}
        }
    }
    pt = request.patch_scheme(url,data_name,schema)
    assert pt[0] == None
    assert pt[1] == 200

def test_albums_delete():
    url = gbl.j_site+"/albums/"
    assert request.delete(url) == 200


