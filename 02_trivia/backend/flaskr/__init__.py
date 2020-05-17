import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random


from models import setup_db, Question, Category
from flask_cors import CORS

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)

  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  CORS(app)
  #cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

  '''
  @TODO:
  Create an endpoint to handle GET requests
  for all available categories.
  '''
  @app.route('/categories',methods=['GET'])
  def show_categories():
    categories = { category.id : category.type for category in Category.query.order_by('id').all() }

    return jsonify({
        'categories' : categories
      })


  '''
  @TODO:
  Create an endpoint to handle GET requests for questions,
  including pagination (every 10 questions).
  This endpoint should return a list of questions,
  number of total questions, current category, categories.

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions.
  '''

  def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start =  (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions

  @app.route('/questions', methods=['GET'])
  def show_questions():
    selection = Question.query.order_by('id').all()

    current_questions = paginate_questions(request,selection)

    if len(current_questions)==0:
      abort(404)

    return jsonify({
      'success': True,
      'questions': current_questions,
      'total_questions': len(selection),
      'categories' : { category.id : category.type for category in Category.query.order_by('id').all() },
      'current_category' : 'ALL'
    })

  '''
  @TODO:
  Create an endpoint to DELETE question using a question ID.

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page.
  '''
  @app.route('/questions/<question_id>', methods=['DELETE'])
  def delete_question(question_id):
    question = Question.query.get(question_id)

    if question is None:
      abort(404)

    question.delete()

    return jsonify({
        "id" : question_id,
        "success" : True
      })

  '''
  @TODO:
  Create an endpoint to POST a new question,
  which will require the question and answer text,
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab,
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.
  '''
  @app.route('/questions', methods=['POST'])
  def add_question():
    try:
      question = request.get_json()['question']
      answer = request.get_json()['answer']
      category = request.get_json()['category']
      difficulty = request.get_json()['difficulty']
      question_obj = Question(question,answer,category,difficulty)
      question_obj.insert()
      return jsonify({
          "success" : True
        })
    except:
      abort(400)

  '''
  @TODO:
  Create a POST endpoint to get questions based on a search term.
  It should return any questions for whom the search term
  is a substring of the question.

  TEST: Search by any phrase. The questions list will update to include
  only question that include that string within their question.
  Try using the word "title" to start.
  '''
  @app.route('/questions/search', methods=['POST'])
  def search_questions():

    search_term = request.get_json()['searchTerm']

    selection = Question.query.filter(Question.question.ilike(f'%{search_term}%'))

    current_questions = paginate_questions(request,selection)

    if len(current_questions)==0:
      abort(404)

    return jsonify({
      'success': True,
      'questions': current_questions,
      'total_questions': Question.query.filter(Question.question.ilike(f'%{search_term}%')).count(),
      'current_category' : 'ALL'
    })

  '''
  @TODO:
  Create a GET endpoint to get questions based on category.

  TEST: In the "List" tab / main screen, clicking on one of the
  categories in the left column will cause only questions of that
  category to be shown.
  '''
  @app.route('/categories/<category_id>/questions', methods=['GET'])
  def show_question_by_category(category_id):
    category = Category.query.get(category_id)
    selection = Question.query.filter_by(category=category_id).all()

    current_questions = paginate_questions(request,selection)

    if len(current_questions)==0:
      abort(404)

    return jsonify({
      'success': True,
      'questions': current_questions,
      'total_questions': len(selection),
      'current_category' : category.type
    })



  '''
  @TODO:
  Create a POST endpoint to get questions to play the quiz.
  This endpoint should take category and previous question parameters
  and return a random questions within the given category,
  if provided, and that is not one of the previous questions.

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not.
  '''
  @app.route('/quizzes', methods=['POST'])
  def play_quiz():
    quiz_category = request.get_json()['quiz_category']
    previous_questions = request.get_json()['previous_questions']

    try :
      if quiz_category['id']==0:
          questions_list = [question.id for question in Question.query.filter(Question.id.notin_(previous_questions))]
      else:
          questions_list = [question.id for question in Question.query.filter(Question.id.notin_(previous_questions), Question.category==quiz_category['id'])]


      if len(questions_list)==0:
        question=None
      else:
        random_question_id = random.choice(questions_list)
        question = Question.query.get(random_question_id).format()

      return jsonify({
          'previous_questions' : previous_questions,
          'question' : question
        })
    except:
      abort(422)
  '''
  @TODO:
  Create error handlers for all expected errors
  including 404 and 422.
  '''
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      "success": False,
      "error": 404,
      "message": "resource not found"
      }), 404

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False,
      "error": 422,
      "message": "unprocessable"
      }), 422

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      "success": False,
      "error": 400,
      "message": "bad request"
      }), 400

  return app

