# Coffee Shop Full Stack

## Full Stack Nano - IAM Final Project

Udacity has decided to open a new digitally enabled cafe for students to order drinks, socialize, and study hard. But they need help setting up their menu experience.

You have been called on to demonstrate your newly learned skills to create a full stack drink menu application. The application must:

1) Display graphics representing the ratios of ingredients in each drink.
2) Allow public users to view drink names and graphics.
3) Allow the shop baristas to see the recipe information.
4) Allow the shop managers to create new drinks and edit existing drinks.

## Getting Started

### Pre-requisites and Local Development 
Developers using this project should already have Python3, pip and node installed on their local machines.

#### Backend

From the backend folder run `pip install requirements.txt`. All required packages are included in the requirements file. 

To run the application run the following commands: 
```
export FLASK_APP=api.py
export FLASK_ENV=development
flask run
```


The application is run on `http://127.0.0.1:5000/` by default and is a proxy in the frontend configuration. 

#### Frontend

From the frontend folder, run the following commands to start the client: 
```
npm install // only once to install dependencies
iconic serve 
```

By default, the frontend will run on http://localhost:8100/. 


## API Reference

### Getting Started
- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:5000/`, which is set as a proxy in the frontend configuration. 
- Authentication: This version of the application does not require authentication or API keys. 

### Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```
The API will return three error types when requests fail:
- 400: Bad Request
- 404: Resource Not Found
- 422: Not Processable 

### Endpoints 
#### GET /drinks
- General:
    - Returns a list of drinks objects and success value
- Sample: `curl http://127.0.0.1:5000/drinks`

``` 
{
    "drinks": [
        {
            "id": 1,
            "recipe": [
                {
                    "color": "grey",
                    "parts": 1
                },
                {
                    "color": "green",
                    "parts": 3
                }
            ],
            "title": "matcha shake"
        },
        {
            "id": 2,
            "recipe": [
                {
                    "color": "grey",
                    "parts": 3
                },
                {
                    "color": "brown",
                    "parts": 1
                }
            ],
            "title": "flatwhite"
        },
        {
            "id": 3,
            "recipe": [
                {
                    "color": "white",
                    "parts": 1
                },
                {
                    "color": "grey",
                    "parts": 2
                }
            ],
            "title": "cap"
        },
        {
            "id": 4,
            "recipe": [
                {
                    "color": "blue",
                    "parts": 1
                }
            ],
            "title": "Blueberry shots"
        }
    ],
    "success": true
}
```

#### GET /drinks-detail
- General:
    - Returns a list of drinks objects and success value
    - require the 'get:drinks-detail' permission
- Sample: `curl http://127.0.0.1:5000/drinks-detail`

``` 
{
    "drinks": [
        {
            "id": 1,
            "recipe": [
                {
                    "color": "grey",
                    "name": "milk",
                    "parts": 1
                },
                {
                    "color": "green",
                    "name": "matcha",
                    "parts": 3
                }
            ],
            "title": "matcha shake"
        },
        {
            "id": 2,
            "recipe": [
                {
                    "color": "grey",
                    "name": "milk",
                    "parts": 3
                },
                {
                    "color": "brown",
                    "name": "coffee",
                    "parts": 1
                }
            ],
            "title": "flatwhite"
        },
        {
            "id": 3,
            "recipe": [
                {
                    "color": "white",
                    "name": "foam",
                    "parts": 1
                },
                {
                    "color": "grey",
                    "name": "milk",
                    "parts": 2
                }
            ],
            "title": "cap"
        },
        {
            "id": 4,
            "recipe": [
                {
                    "color": "blue",
                    "name": "blue pine",
                    "parts": 1
                }
            ],
            "title": "Blueberry shots"
        }
    ],
    "success": true
}
```

#### POST /drinks
- General:
    - Creates a new drink using the submitted title and receipe. Returns the drink object of the created drink and success value
- Sample : 
    `curl http://127.0.0.1:5000/drinks -X POST -H "Content-Type: application/json" -d '{"recipe": [{"color": "pink","name" : "berry          cream","parts": 3}],"title": "match strawberry milkshake"}'`
```
{
    "drinks": {
        "id": 8,
        "recipe": [
            {
                "color": "pink",
                "name": "berry cream",
                "parts": 3
            }
        ],
        "title": "match strawberry milkshake"
    },
    "success": true
}
```

#### DELETE /drinks/{drink_id}
- General:
    - Deletes the drink of the given ID if it exists. Returns the id of the deleted drink and success value
- Sample: `curl -X DELETE http://127.0.0.1:5000/questions/1`
```
{
    "delete": "1",
    "success": true
}
```

#### PATCH /drinks/{drink_id}
- General:
    - If provided, updates the attributes of the specified drink. Returns the success value and id of the modified book. 
- Sample: `curl http://127.0.0.1:5000/drinks/2 -X PATCH -H "Content-Type: application/json" -d '{"recipe": [{ "color": "grey","parts":             3},{"color": "yellow","parts": 1}],"title": "flatwhite"}'`
```
{
    "drinks": [
        {
            "id": 2,
            "recipe": [
                {
                    "color": "grey",
                    "parts": 3
                },
                {
                    "color": "yellow",
                    "parts": 1
                }
            ],
            "title": "flatwhite"
        },
        {
            "id": 3,
            "recipe": [
                {
                    "color": "white",
                    "name": "foam",
                    "parts": 1
                },
                {
                    "color": "grey",
                    "name": "milk",
                    "parts": 2
                }
            ],
            "title": "cap"
        },
        {
            "id": 4,
            "recipe": [
                {
                    "color": "blue",
                    "name": "blue pine",
                    "parts": 1
                }
            ],
            "title": "Blueberry shots"
        },
        {
            "id": 5,
            "recipe": [
                {
                    "color": "green",
                    "name": "mohitto",
                    "parts": 1
                }
            ],
            "title": "Matcha"
        },
        {
            "id": 6,
            "recipe": [
                {
                    "color": "green",
                    "name": "matcha",
                    "parts": 2
                },
                {
                    "color": "pink",
                    "name": "berries",
                    "parts": 2
                }
            ],
            "title": "match strawberry"
        }
    ],
    "success": true
}
```


## Deployment N/A

## Authors
Palak Dhingra 

## Acknowledgements 
The awesome team at Udacity! 
