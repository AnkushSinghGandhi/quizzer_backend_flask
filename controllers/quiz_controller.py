from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime
from ..models.quiz_model import Quiz
from .. import db

quiz_bp = Blueprint('quiz', __name__)

@quiz_bp.route('/quizzes', methods=['POST'])
@jwt_required()
def create_quiz():
    data = request.get_json()
    new_quiz = Quiz(
        title=data['title'],
        description=data.get('description'),
        category_id=data['category_id'],
        end_date=datetime.strptime(data['end_date'], '%Y-%m-%d %H:%M:%S') if 'end_date' in data else None
    )
    db.session.add(new_quiz)
    db.session.commit()
    return jsonify({'message': 'Quiz created successfully!'})

@quiz_bp.route('/quizzes', methods=['GET'])
def get_quizzes():
    quizzes = Quiz.query.all()
    output = []
    for quiz in quizzes:
        quiz_data = {
            'id': quiz.id,
            'title': quiz.title,
            'description': quiz.description,
            'category': quiz.category.name,
            'creation_date': quiz.creation_date,
            'end_date': quiz.end_date
        }
        output.append(quiz_data)
    return jsonify({'quizzes': output})
