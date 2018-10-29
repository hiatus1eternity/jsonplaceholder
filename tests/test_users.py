import pytest

import requests
from json_payload_validator import validate
import logging
import json
from utils import req
logging.basicConfig(level=logging.DEBUG)

j_site = 'https://jsonplaceholder.typicode.com'

def test_users_get():
    schema = {
        "type": "array",
        "properties": {
            "id": {"type": "integer","minimum":1,"uniqueItems": True},
            "name":{"type":"string"},
            "username":{"type":"string"},
            "email": {"type": "string","format":"email"},
            "address": {"type": "object",
                        "properties":{
                            "street":{"type":"string"},
                            "suite":{"type":"string"},
                            "city":{"type":"string"},
                            "zipcode":{"type":"string"},
                            "geo":{"type":"object",
                                   "properties":{
                                       "lat":{"type":"string"},
                                       "lng":{"type":"string"}
                                        }
                                   }
                            }
                        },
            "phone":{"type":"string"},
            "website":{"type":"string"},
            "company":{"type":"object",
                       "properties":{
                           "name":{"type":"string"},
                           "catchPhrase":{"type":"string"},
                           "bs":{"type":"string"}
                            }
                       }
        }
    }
    r = requests.get(j_site+"/users")
    error = validate(r.json(), schema)
    assert error == None
    assert r.status_code == 200

def test_users_last_get():
    url = j_site+"/users/"
    l = req.json_lenght(url)
    url = url+str(l)
    r = requests.get(url)
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer","value":l},
            "name":{"type":"string"},
            "username":{"type":"string"},
            "email": {"type": "string","format":"email"},
            "address": {"type": "object",
                        "properties":{
                            "street":{"type":"string"},
                            "suite":{"type":"string"},
                            "city":{"type":"string"},
                            "zipcode":{"type":"string"},
                            "geo":{"type":"object",
                                   "properties":{
                                       "lat":{"type":"string"},
                                       "lng":{"type":"string"}
                                        }
                                   }
                            }
                        },
            "phone":{"type":"string"},
            "website":{"type":"string"},
            "company":{"type":"object",
                       "properties":{
                           "name":{"type":"string"},
                           "catchPhrase":{"type":"string"},
                           "bs":{"type":"string"}
                            }
                       }
        }
    }
    error = validate(r.json(), schema)
    assert error == None
    assert r.status_code == 200

def test_users_post():
    url = j_site+"/users/"
    userId = req.json_lenght(url)
    r = requests.post(j_site+"/users",json=  {"name": "Glenna Reichert","username": "Delphine", "email": "Chaim_McDermott@dana.io", "address": {
                                                                "street": "Dayna Park",
                                                                "suite": "Suite 449",
                                                                "city": "Bartholomebury",
                                                                "zipcode": "76495-3109",
                                                                "geo": {
                                                                        "lat": "24.6463",
                                                                        "lng": "-168.8889"
                                                                        }
                                                            },
                                                "phone": "(775)976-6794 x41206",
                                                "website": "conrad.com",
                                                "company": {
                                                  "name": "Yost and Sons",
                                                  "catchPhrase": "Switchable contextually-based project",
                                                  "bs": "aggregate real-time technologies"
                                                            }
                                              }
                      )
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer","value":userId+1},
            "name":{"type":"string","value":"Glenna Reichert"},
            "username":{"type":"string","value":"Delphine"},
            "email": {"type": "string","format":"email"},
            "address": {"type": "object",
                        "properties":{
                            "street":{"type":"string"},
                            "suite":{"type":"string"},
                            "city":{"type":"string"},
                            "zipcode":{"type":"string"},
                            "geo":{"type":"object",
                                   "properties":{
                                       "lat":{"type":"string"},
                                       "lng":{"type":"string"}
                                        }
                                   }
                            }
                        },
            "phone":{"type":"string"},
            "website":{"type":"string"},
            "company":{"type":"object",
                       "properties":{
                           "name":{"type":"string"},
                           "catchPhrase":{"type":"string"},
                           "bs":{"type":"string"}
                            }
                       }
        }
    }
    error = validate(r.json(), schema)
    assert error == None
    assert r.status_code == 201

def test_users_put():
    url = j_site+"/users/"
    l = req.json_lenght(url)
    r = requests.put(j_site+"/users/"+str(l),json={"name": "Glenna Reichert","username": "Delphine","email": "Chaim_McDermott@dana.io","address": {"street":"Dayna Park","suite":"Suite 449","city":"Bartholomebury","zipcode":"76495-3109","geo": {"lat": "24.6463","lng": "-168.8889"}},"phone": "(775)976-6794 x41206","website": "conrad.com","company": {"name": "Yost and Sons","catchPhrase": "Switchable contextually-based project","bs": "aggregate real-time technologies"}})
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer","value":l},
            "name":{"type":"string"},
            "username":{"type":"string","value":"Delphine"},
            "email": {"type": "string","format":"email"},
            "address": {"type": "object",
                        "properties":{
                            "street":{"type":"string"},
                            "suite":{"type":"string"},
                            "city":{"type":"string"},
                            "zipcode":{"type":"string"},
                            "geo":{"type":"object",
                                   "properties":{
                                       "lat":{"type":"string"},
                                       "lng":{"type":"string"}
                                        }
                                   }
                            }
                        },
            "phone":{"type":"string"},
            "website":{"type":"string"},
            "company":{"type":"object",
                       "properties":{
                           "name":{"type":"string"},
                           "catchPhrase":{"type":"string"},
                           "bs":{"type":"string"}
                            }
                       }
        }
    }
    error = validate(r.json(), schema)
    assert error == None
    assert r.status_code == 200

def test_users_patch():
    url = j_site+"/users/"
    l = req.json_lenght(url)
    r = requests.patch(j_site+"/users/"+str(l),data={"name":"post_19:55"})
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer","value":l},
            "name":{"type":"string", "value":"post_19:55"},
            "username":{"type":"string"},
            "email": {"type": "string","format":"email"},
            "address": {"type": "object",
                        "properties":{
                            "street":{"type":"string"},
                            "suite":{"type":"string"},
                            "city":{"type":"string"},
                            "zipcode":{"type":"string"},
                            "geo":{"type":"object",
                                   "properties":{
                                       "lat":{"type":"string"},
                                       "lng":{"type":"string"}
                                        }
                                   }
                            }
                        },
            "phone":{"type":"string"},
            "website":{"type":"string"},
            "company":{"type":"object",
                       "properties":{
                           "name":{"type":"string"},
                           "catchPhrase":{"type":"string"},
                           "bs":{"type":"string"}
                            }
                       }
        }
    }
    error = validate(r.json(), schema)
    assert error == None
    assert r.status_code == 200

def test_comments_delete():
    url = j_site+"/users/"
    l = req.json_lenght(url)
    url = j_site + "/users/" + str(l)
    r = requests.delete(url)
    assert r.status_code == 200