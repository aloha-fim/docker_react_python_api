"# docker_react_python_api" 

# API routes
## API routes found in /swagger-ui and jwt in /jwt.io

## Create a Store Event
```
- POST /store_event {"name": "PMI Hawaii"}

- response {"name": "PMI Hawaii", "items": [ ]}
```

## Create Items in an Event
```
- POST /store_event/<PMI Hawaii>/item {"name": "Keynote Speaker X", "price": 5000}

- response {"name": "Keynote Speaker X", "price": 5000}
```

## Get all Store Events and Items in each Event
```
- GET /store_event/

- response { "stores": [
    {
        "name": "PMI Hawaii",
        "items": [
            {
                "name": "Keynote Speaker X",
                "price": 5000
            }
        ]
    }
]}
```

## Get particular Store Event
```
- GET /store_event/<PMI Hawaii>

- response {
        "name": "PMI Hawaii",
        "items": [
            {
                "name": "Keynote Speaker X",
                "price": 5000
            }
        ]
    }
```

## Get only items in each Store Event
```
- GET /store_event/<PMI Hawaii>/item

- response [
        {
            "name": "Keynote Speaker X",
            "price": 5000
        }
    ]
```

## Get list of tags in each Store Event
```
- GET /store_event/<PMI Hawaii>/tag

- response [
        {
            
        }
    ]
```

## Create a new tag in each Store Event
```
- POST /store_event/<PMI Hawaii>/tag

- response [
        {
            
        }
    ]
```

## Link an item in a Store Event with a tag from the same Store Event
```
- POST /item/<item_id>/tag/<tag_id>

- response [
        {
            
        }
    ]
```

## Unlink a tag from an item
```
- DELETE /item/<item_id>/tag/<tag_id>

- response [
        {
            
        }
    ]
```

## Get tag info
```
- GET /tag/<tag_id>

- response [
        {
            
        }
    ]
```

## Delete tag
```
- DELETE /tag/<tag_id>

- response [
        {
             
        }
    ]
```

## Create user accounts given email and password
```
- POST /register

- response [
        {
             
        }
    ]
```

## Login and get JWT given email and password
```
- POST /login

- response [
        {
             
        }
    ]
```

## Logout and revoke JWT
```
- POST /logout

- response [
        {
             
        }
    ]
```

## Get a fresh JWT
```
- POST /refresh

- response [
        {
             
        }
    ]
```

# Start Up

## turn on virtual environment in Windows
- py -m venv .venv
- CTRL+SH P  "terminal venv" 
- CTRL J "activate venv"

## run docker
- docker build -t rest-apis-flask-python . "build docker"
- docker run -d -p 5005:5000 rest-apis-flask-python "via cl run deamon docker"

## install flask-migrate
- cmd: flask db init
- flask db migrate
- flask db upgrade

# change model
- flask db migrate
- flask db upgrade


