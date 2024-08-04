from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models.question_model import Question
from models.choice_model import Choice
from app import db

question_bp = Blueprint('question', __name__)

@question_bp.route('/quizzes/<quiz_id>/questions', methods=['POST'])
@jwt_required()
def add_question(quiz_id):
    data = request.get_json()
    new_question = Question(
        question_text=data['question_text'],
        quiz_id=quiz_id
    )
    db.session.add(new_question)
    db.session.commit()
    return jsonify({'message': 'Question added successfully!'})

@question_bp.route('/questions/<question_id>/answers', methods=['POST'])
@jwt_required()
def add_choice(question_id):
    data = request.get_json()
    new_answer = Choice(
        answer_text=data['answer_text'],
        is_correct=data['is_correct'],
        question_id=question_id
    )
    db.session.add(new_answer)
    db.session.commit()
    return jsonify({'message': 'Answer added successfully!'})
