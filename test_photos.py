import pytest

import requests
from json_payload_validator import validate
import logging
import json
from utils import req

logging.basicConfig(level=logging.DEBUG)


j_site = 'https://jsonplaceholder.typicode.com'

def test_photos_get():
    schema = {
        "type": "array",
        "properties": {
            "albumId": {"type": "integer","minimum":1},
            "id": {"type": "integer","minimum":1,"uniqueItems": True},
            "title": {"type": "string"},
            "url": {"type": "string","format":"uri"},
            "thumbnailUrl": {"type": "string","format":"uri"}
        }
    }
    r = requests.get(j_site+"/photos")
    error = validate(r.json(), schema)
    assert error == None
    assert r.status_code == 200

def test_photos_last_get():
    url = j_site+"/photos/"
    l = req.json_lenght(url)
    r = requests.get(url+str(l))
    schema = {
        "type": "object",
        "properties": {
            "albumId": {"type": "integer"},
            "id": {"type": "integer","value":l},
            "title": {"type": "string"},
            "url": {"type": "string","format":"uri"},
            "thumbnailUrl": {"type": "string","format":"uri"}
        }
    }
    error = validate(r.json(), schema)
    assert error == None
    assert r.status_code == 200

def test_photos_albums_get():
    url = j_site+"/albums/"
    l = req.json_lenght(url)
    payload = {"albumId":l}
    r = requests.get(j_site+"/photos", params=payload)
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
    assert error == None
    assert r.status_code == 200

def test_photos_post():
    url = j_site+"/albums/"
    l = req.json_lenght(url)
    url = j_site+"/photos/"
    pho = req.json_lenght(url)
    r = requests.post(j_site+"/photos",data={"title":"post_19:55","url":"https://azcxards.net/3/1","thumbnailUrl":"https://azcxards.net/3/1","albumId":l})
    schema = {
    "type": "object",
    "properties": {
        "albumId": {"type": "string","value":l},
        "id": {"type": "integer", "value":pho+1},
        "title": {"type": "string","value":"post_19:55"},
        "url": {"type": "string","value":"https://azcxards.net/3/1"},
        "thumbnailUrl": {"type": "string","value":"https://azcxards.net/3/1"}
    }
    }
    error = validate(r.json(), schema)
    assert error == None
    assert r.status_code == 201

def test_photos_put():
    url = j_site+"/albums/"
    l = req.json_lenght(url)
    url = j_site+"/photos/"
    pho = req.json_lenght(url)
    r = requests.put(j_site+"/photos/"+str(pho),data={"title":"post_19:55","url":"https://azcxards.net/3/1","thumbnailUrl":"https://azcxards.net/3/1","albumId":l,"id":pho})
    schema = {
    "type": "object",
    "properties": {
        "albumId": {"type": "string","value":l},
        "id": {"type": "integer", "value":pho},
        "title": {"type": "string","value":"post_19:55"},
        "url": {"type": "string","value":"https://azcxards.net/3/1"},
        "thumbnailUrl": {"type": "string","value":"https://azcxards.net/3/1"}
        }
    }
    error = validate(r.json(), schema)
    assert error == None
    assert r.status_code == 200

def test_photos_patch():
    url = j_site+"/photos/"
    pho = req.json_lenght(url)
    r = requests.patch(j_site+"/photos/"+str(pho),data={"title":"post_19:55"})
    schema = {
    "type": "object",
    "properties": {
        "albumId": {"type": "integer"},
        "id": {"type": "integer", "value":pho},
        "title": {"type": "string","value":"post_19:55"},
        "url": {"type": "string"},
        "thumbnailUrl": {"type": "string"}
        }
    }
    error = validate(r.json(), schema)
    assert error == None
    assert r.status_code == 200

def test_photos_delete():
    url = j_site+"/photos/"
    pho = req.json_lenght(url)
    url = j_site + "/photos/" + str(pho)
    r = requests.delete(url)
    assert r.status_code == 200