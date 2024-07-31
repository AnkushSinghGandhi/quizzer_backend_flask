from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from datetime import datetime
from ..models.quiz_model import Quiz
from .. import db
from ..decorators import admin_required

quiz_bp = Blueprint('quiz', __name__)

@quiz_bp.route('/quizzes', methods=['POST'])
@jwt_required()
@admin_required
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

@quiz_bp.route('/quizzes/<int:quiz_id>', methods=['PUT'])
@jwt_required()
@admin_required
def edit_quiz(quiz_id):
    data = request.get_json()
    quiz = Quiz.query.get_or_404(quiz_id)
    quiz.title = data.get('title', quiz.title)
    quiz.description = data.get('description', quiz.description)
    quiz.category_id = data.get('category_id', quiz.category_id)
    quiz.end_date = datetime.strptime(data['end_date'], '%Y-%m-%d %H:%M:%S') if 'end_date' in data else quiz.end_date
    db.session.commit()
    return jsonify({'message': 'Quiz updated successfully!'})

@quiz_bp.route('/quizzes/<int:quiz_id>', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    db.session.delete(quiz)
    db.session.commit()
    return jsonify({'message': 'Quiz deleted successfully!'})

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

@quiz_bp.route('/quizzes/category/<int:category_id>', methods=['GET'])
@jwt_required()
def get_quizzes_by_category(category_id):
    quizzes = Quiz.query.filter_by(category_id=category_id).all()
    
    output = [
        {
            'id': quiz.id,
            'title': quiz.title,
            'description': quiz.description,
            'creation_date': quiz.creation_date,
            'end_date': quiz.end_date
        } for quiz in quizzes
    ]
    
    return jsonify({'quizzes': output})
