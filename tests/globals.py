
#url основной страницы и всех главных веток
j_site = 'https://jsonplaceholder.typicode.com'
albums_url = 'https://jsonplaceholder.typicode.com/albums/'
photos_url = 'https://jsonplaceholder.typicode.com/photos/'
comments_url = 'https://jsonplaceholder.typicode.com/comments/'
posts_url = 'https://jsonplaceholder.typicode.com/posts/'
todos_url = 'https://jsonplaceholder.typicode.com/todos/'
users_url = 'https://jsonplaceholder.typicode.com/users/'

#schemes for albums tests
schema_albums_get = {
    "type": "array",
    "properties": {
        "userId": {"type": "integer", "minimum": 1},
        "id": {"type": "integer", "minimum": 1, "uniqueItems": True},
        "title": {"type": "string"}
        }
    }

schema_albums_element_get = {
    "type": "object",
    "properties": {
        "userId": {"type": "integer", "minimum": 1},
        "id": {"type": "integer", "minimum": 1, "uniqueItems": True},
        "title": {"type": "string"}
        }
    }

def schema_albums_phot_get(value):
    return {
        "type": "array",
        "properties": {
            "albumId": {"type": "integer","value":value},
            "url": {"type": "string"},
            "id": {"type": "integer", "minimum": 1, "uniqueItems": True},
            "title": {"type": "string"},
            "thumbnailUrl": {"type": "string"}
            }
        }

def schema_albums_user_get(value):
    return {
        "type": "array",
        "properties": {
            "userId":{"type":"integer","value":value},
            "id": {"type": "integer","minimum":1,"uniqueItems": True},
            "title": {"type": "string"}
            }
        }

def schema_albums_post(userid,id):
    return {
        "type": "object",
        "properties": {
            "userId": {"type": "string","value":userid},
            "id": {"type": "integer", "value":id},
            "title": {"type": "string","value":"post_19:55"}
            }
        }

def schema_albums_patch(id):
    return {
        "type": "object",
        "properties": {
            "userId": {"type": "integer"},
            "id": {"type": "integer", "value":id},
            "title": {"type": "string","value":"post_19:55"}
            }
        }

#schemes for comments tests
scheme_comments_get = {
    "type": "array",
    "properties": {
        "postId": {"type": "integer","minimum":1},
        "id": {"type": "integer","minimum":1,"uniqueItems": True},
        "name":{"type":"string"},
        "email": {"type": "string","format":"email"},
        "body": {"type": "string"}
        }
    }

schema_comments_element_get = {
    "type": "object",
    "properties": {
        "postId": {"type": "integer"},
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "body": {"type": "string"}
        }
    }

def schema_comments_postId_get(value):
    return {
        "type": "array",
        "properties": {
            "postId": {"type": "integer", "value": value},
            "name": {"type": "string"},
            "id": {"type": "integer", "minimum": 1, "uniqueItems": True},
            "title": {"type": "string"},
            "body": {"type": "string"}
            }
        }

def schema_comments_post(postId,id):
    return {
        "type": "object",
        "properties": {
            "postId": {"type": "string","value":postId},
            "id": {"type": "integer", "value":id},
            "name": {"type": "string","value":"post_19:55"},
            "body": {"type": "string","value":"this is simple new post by me"},
            "email": {"type": "string", "format": "email","value":"my@my.my"}
            }
        }

def schema_comments_patch(id):
    return {
        "type": "object",
        "properties": {
            "postId": {"type": "integer"},
            "id": {"type": "integer","value":id},
            "name": {"type": "string","value":"post_19:55"},
            "body": {"type": "string"},
            "email": {"type": "string", "format": "email"}
            }
        }

#schemes for photos tests
schema_photos_get = {
    "type": "array",
    "properties": {
        "albumId": {"type": "integer","minimum":1},
        "id": {"type": "integer","minimum":1,"uniqueItems": True},
        "title": {"type": "string"},
        "url": {"type": "string","format":"uri"},
        "thumbnailUrl": {"type": "string","format":"uri"}
        }
    }

schema_photos_element_get = {
    "type": "object",
    "properties": {
        "albumId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "url": {"type": "string", "format": "uri"},
        "thumbnailUrl": {"type": "string", "format": "uri"}
        }
    }

def schema_photos_albumid_get(value):
    return {
        "type": "array",
        "properties": {
            "albumId":{"type":"integer","value":value},
            "url":{"type": "string"},
            "id": {"type": "integer","minimum":1},
            "title": {"type": "string"},
            "thumbnailUrl": {"type": "string"}
            }
        }

def schema_photos_post(albumid,id):
    return {
        "type": "object",
        "properties": {
            "albumId": {"type": "string","value":albumid},
            "id": {"type": "integer", "value":id},
            "title": {"type": "string","value":"post_19:55"},
            "url": {"type": "string","value":"https://azcxards.net/3/1"},
            "thumbnailUrl": {"type": "string",
                             "value":"https://azcxards.net/3/1"}
            }
        }

def schema_photos_patch(id):
    return {
        "type": "object",
        "properties": {
            "albumId": {"type": "integer"},
            "id": {"type": "integer","value":id},
            "title": {"type": "string", "value": "post_19:55"},
            "url": {"type": "string"},
            "thumbnailUrl": {"type": "string"}
            }
        }

#schemes for posts tests
schema_posts_get = {
    "type": "array",
    "properties": {
        "userId": {"type": "integer","minimum":1},
        "id": {"type": "integer","minimum":1,"uniqueItems": True},
        "title": {"type": "string"},
        "body": {"type": "string"}
        }
    }

schema_posts_element_get = {
        "type": "object",
        "properties": {
            "userId": {"type": "integer"},
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "body": {"type": "string"}
            }
        }

def schema_posts_comments_get(value):
    return {
        "type": "array",
        "properties": {
            "postId": {"type": "integer", "value": value},
            "name": {"type": "string"},
            "id": {"type": "integer", "minimum": 1},
            "title": {"type": "string"},
            "body": {"type": "string"}
            }
        }

def schema_posts_user_get(value):
    return {
        "type": "array",
        "properties": {
            "userId": {"type": "integer", "value": value},
            "id": {"type": "integer", "minimum": 1},
            "title": {"type": "string"},
            "body": {"type": "string"}
            }
        }

def schema_posts_post(userId,id):
    return {
        "type": "object",
        "properties": {
            "userId": {"type": "string", "value": userId},
            "id": {"type": "integer", "value": id},
            "title": {"type": "string", "value": "post_19:55"},
            "body": {"type": "string",
                     "value": "this is simple new post by me"}
            }
        }

def schema_posts_patch(value):
    return {
        "type": "object",
        "properties": {
            "userId": {"type": "integer"},
            "id": {"type": "integer","value":value},
            "title": {"type": "string", "value": "post_19:55"},
            "body": {"type": "string"}
            }
        }

#schemes for todos
schema_todos_get = {
    "type": "array",
    "properties": {
        "userId": {"type": "integer","minimum":1},
        "id": {"type": "integer","minimum":1,"uniqueItems": True},
        "title": {"type": "string"},
        "completed": {"type": "boolean"}
        }
    }

schema_todos_element_get = {
        "type": "object",
        "properties": {
            "userId": {"type": "integer"},
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "completed": {"type": "boolean"}
            }
        }

def schema_todos_user_get(value):
    return {
        "type": "array",
        "properties": {
            "userId": {"type": "integer", "value": value},
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "completed": {"type": "boolean"}
            }
        }

def schema_todos_post(userId,id):
    return  {
        "type": "object",
        "properties": {
            "userId": {"type": "string","value":userId},
            "id": {"type": "integer", "value": id},
            "title": {"type": "string", "value": "post_19:55"},
            "completed": {"type": "string"}
            }
        }

def schema_todos_patch(value):
    return {
        "type": "object",
        "properties": {
            "userId": {"type": "integer"},
            "id": {"type": "integer","value":value},
            "title": {"type": "string","value":"post_19:55"},
            "completed": {"type": "boolean"}
            }
        }

#schemes for users
schema_users_get = {
    "type": "array",
    "properties": {
        "id": {"type": "integer","minimum":1,"uniqueItems": True},
        "name":{"type":"string"},
        "username":{"type":"string"},
        "email": {"type": "string","format":"email"},
        "address": {
            "type": "object",
            "properties":{
                "street":{"type":"string"},
                "suite":{"type":"string"},
                "city":{"type":"string"},
                "zipcode":{"type":"string"},
                "geo":{
                    "type":"object",
                    "properties":{
                        "lat":{"type":"string"},
                        "lng":{"type":"string"}
                        }
                    }
                }
            },
        "phone":{"type":"string"},
        "website":{"type":"string"},
        "company":{
            "type":"object",
            "properties":{
                "name":{"type":"string"},
                "catchPhrase":{"type":"string"},
                "bs":{"type":"string"}
                }
            }
        }
    }

schema_users_element_get = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name":{"type":"string"},
        "username":{"type":"string"},
        "email": {"type": "string","format":"email"},
        "address": {
            "type": "object",
            "properties":{
                "street":{"type":"string"},
                "suite":{"type":"string"},
                "city":{"type":"string"},
                "zipcode":{"type":"string"},
                "geo":{
                    "type":"object",
                    "properties":{
                        "lat":{"type":"string"},
                        "lng":{"type":"string"}
                        }
                    }
                }
            },
        "phone":{"type":"string"},
        "website":{"type":"string"},
        "company":{
            "type":"object",
            "properties":{
                "name":{"type":"string"},
                "catchPhrase":{"type":"string"},
                "bs":{"type":"string"}
                }
            }
        }
    }

def schema_users_patch(value):
    return {
        "type": "object",
        "properties":{
            "id": {"type": "integer","value":value},
            "name":{"type":"string", "value":"post_19:55"},
            "username":{"type":"string"},
            "email": {"type": "string","format":"email"},
            "address":{
                "type": "object",
                "properties":{
                    "street":{"type":"string"},
                    "suite":{"type":"string"},
                    "city":{"type":"string"},
                    "zipcode":{"type":"string"},
                    "geo":{
                        "type":"object",
                        "properties":{
                            "lat":{"type":"string"},
                            "lng":{"type":"string"}
                            }
                        }
                    }
                },
            "phone":{"type":"string"},
            "website":{"type":"string"},
            "company":{
                "type":"object",
                "properties":{
                    "name":{"type":"string"},
                    "catchPhrase":{"type":"string"},
                    "bs":{"type":"string"}
                    }
                }
            }
        }

def schema_users_post(value):
    return {
        "type": "object",
        "properties":{
            "id": {"type": "integer","value":value},
            "name":{"type":"string"},
            "username":{"type":"string","value":"Delphine"},
            "email": {"type": "string","format":"email"},
            "address":{
                "type": "array",
                "properties":{
                    "street":{"type":"string"},
                    "suite":{"type":"string"},
                    "city":{"type":"string"},
                    "zipcode":{"type":"string"},
                    "geo":{
                        "type":"array",
                        "properties":{
                            "lat":{"type":"string"},
                            "lng":{"type":"string"}
                            }
                        }
                    }
                },
            "phone":{"type":"string"},
            "website":{"type":"string"},
            "company":{
                "type":"array",
                "properties":{
                    "name":{"type":"string"},
                    "catchPhrase":{"type":"string"},
                    "bs":{"type":"string"}
                    }
                }
            }
        }