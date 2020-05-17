# Full Stack API Final Project

## Full Stack Trivia

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a  webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out. 

That's where you come in! Help them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

1) Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer. 
2) Delete questions.
3) Add questions and require that they include question and answer text.
4) Search for questions based on a text query string.
5) Play the quiz game, randomizing either all questions or within a specific category. 


## Getting Started

### Pre-requisites and Local Development 
Developers using this project should already have Python3, pip and node installed on their local machines.

#### Backend

From the backend folder run `pip install requirements.txt`. All required packages are included in the requirements file. 

To run the application run the following commands: 
```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

These commands put the application in development and directs our application to use the `__init__.py` file in our flaskr folder. Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made. If running locally on Windows, look for the commands in the [Flask documentation](http://flask.pocoo.org/docs/1.0/tutorial/factory/).

The application is run on `http://127.0.0.1:5000/` by default and is a proxy in the frontend configuration. 

#### Frontend

From the frontend folder, run the following commands to start the client: 
```
npm install // only once to install dependencies
npm start 
```

By default, the frontend will run on localhost:3000. 

### Tests
In order to run tests navigate to the backend folder and run the following commands: 

```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

The first time you run the tests, omit the dropdb command. 

All tests are kept in that file and should be maintained as updates are made to app functionality. 

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
- `curl http://127.0.0.1:5000/questions?page=1 -X POST -H "Content-Type: application/json" -d '{"answer": "area","category": 2,"difficulty": 1,"id": 4,"question": "The Homolographic projection has the correct representation of"}'`
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
- `curl -X DELETE http://127.0.0.1:5000/questions/4`
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

## Deployment N/A

## Authors
Palak Dhingra 

## Acknowledgements 
The awesome team at Udacity! 


