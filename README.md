"# docker_react_python_api" 

# API routes

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

# Start Up

## turn on virtual environment in Windows
- py -m venv .venv
- CTRL+SH P  "terminal venv" 
- CMD J "activate venv"

docker build -t rest-apis-flask-python . "build docker"
docker run -d -p 5005:5000 rest-apis-flask-python "run deamon docker"

install flask-migrate
cmd: flask db init
flask db migrate
flask db upgrade

#change model
flask db migrate
flask db upgrade


"# python_postgres_api" 
