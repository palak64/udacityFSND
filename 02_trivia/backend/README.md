# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

### Endpoints 
#### GET /questions
- General:
    - Returns a list of question objects, success value, and total number of questions
    - Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1. 
- Sample: `curl http://127.0.0.1:5000/questions`

``` {
    "categories": {
        "1": "Science",
        "2": "Geography",
        "3": "Art",
        "4": "History",
        "5": "Sports",
        "6": "Entertainment"
    },
    "current_category": "ALL",
    "questions": [
        {
            "answer": "Wildflowers",
            "category": 1,
            "difficulty": 2,
            "id": 2,
            "question": "Super Pink Moon gets its name from....."
        },
        {
            "answer": "Richard Nolle",
            "category": 1,
            "difficulty": 1,
            "id": 3,
            "question": "Who coined the term “Supermoon”?"
        }
    ],
    "success": true,
    "total_questions": 2
}
```

#### POST /questions
- General:
    - Creates a new question using the submitted question, answer, category and difficulty. Returns the id of the created question, success value, total questions, and question list based on current page number to update the frontend. 
- Sample: `curl http://127.0.0.1:5000/questions?page=1 -X POST -H "Content-Type: application/json" -d '{"answer": "area","category": 2,"difficulty": 1,"id": 4,"question": "The Homolographic projection has the correct representation of"}'`
```
{
    "categories": {
        "1": "Science",
        "2": "Geography",
        "3": "Art",
        "4": "History",
        "5": "Sports",
        "6": "Entertainment"
    },
    "current_category": "ALL",
    "questions": [
        {
            "answer": "Wildflowers",
            "category": 1,
            "difficulty": 2,
            "id": 2,
            "question": "Super Pink Moon gets its name from....."
        },
        {
            "answer": "Richard Nolle",
            "category": 1,
            "difficulty": 1,
            "id": 3,
            "question": "Who coined the term “Supermoon”?"
        },
        {
            "answer": "area",
            "category": 2,
            "difficulty": 1,
            "id": 4,
            "question": "The Homolographic projection has the correct representation of"
        }
    ],
    "success": true,
    "total_questions": 3
}
```
#### DELETE /questions/{question_id}
- General:
    - Deletes the book of the given ID if it exists. Returns the id of the deleted book, success value, total books, and book list based on current page number to update the frontend. 
- Sample : `curl -X DELETE http://127.0.0.1:5000/questions/4`
```
{
    "categories": {
        "1": "Science",
        "2": "Geography",
        "3": "Art",
        "4": "History",
        "5": "Sports",
        "6": "Entertainment"
    },
    "current_category": "ALL",
    "questions": [
        {
            "answer": "Wildflowers",
            "category": 1,
            "difficulty": 2,
            "id": 2,
            "question": "Super Pink Moon gets its name from....."
        },
        {
            "answer": "Richard Nolle",
            "category": 1,
            "difficulty": 1,
            "id": 3,
            "question": "Who coined the term “Supermoon”?"
        }
    ],
    "success": true,
    "total_questions": 2
}
```
#### GET /categories
- General:
    - Returns a list of categories objects.
- Sample: `curl http://127.0.0.1:5000/categories`
```
{
    "categories": {
        "1": "Science",
        "2": "Geography",
        "3": "Art",
        "4": "History",
        "5": "Sports",
        "6": "Entertainment"
    }
}
```

#### GET /categories/<category_id>/questions
- General:
    - Returns a list of questions in a category.
- Sample: `curl http://127.0.0.1:5000/categories/1/questions`
```
{
    "current_category": "Science",
    "questions": [
        {
            "answer": "Wildflowers",
            "category": 1,
            "difficulty": 2,
            "id": 2,
            "question": "Super Pink Moon gets its name from....."
        },
        {
            "answer": "Richard Nolle",
            "category": 1,
            "difficulty": 1,
            "id": 3,
            "question": "Who coined the term “Supermoon”?"
        }
    ],
    "success": true,
    "total_questions": 2
}
```

#### POST /questions/search
- General:
    - Returns a list of questions matching the search pattern in a question.
- Sample: `curl http://127.0.0.1:5000/questions/search -X POST -H "Content-Type: application/json" -d '{"searchTerm": "moon"}' `
```
{
    "current_category": "ALL",
    "questions": [
        {
            "answer": "Wildflowers",
            "category": 1,
            "difficulty": 2,
            "id": 2,
            "question": "Super Pink Moon gets its name from....."
        },
        {
            "answer": "Richard Nolle",
            "category": 1,
            "difficulty": 1,
            "id": 3,
            "question": "Who coined the term “Supermoon”?"
        }
    ],
    "success": true,
    "total_questions": 2
}
```

#### POST /quizzes
- General:
    - This endpoint should take category and previous question parameters and return a random questions within the given category, if         provided, and that is not one of the previous questions.
- Sample: `curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions":[],"quiz_category":       {"type": "Geography", "id": "2"}}' `
```
{
    "previousQuestions": null,
    "question": {
        "answer": "area",
        "category": 2,
        "difficulty": 1,
        "id": 4,
        "question": "The Homolographic projection has the correct representation of"
    }
}
```

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

## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
