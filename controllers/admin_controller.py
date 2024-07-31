from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from ..models.user_model import User
from ..models.score_model import Score
from .. import db
from ..decorators import admin_required

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/users', methods=['GET'])
@jwt_required()
@admin_required
def get_users():
    users = User.query.all()
    output = []
    for user in users:
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'role': user.role
        }
        output.append(user_data)
    return jsonify({'users': output})

@admin_bp.route('/users/<int:user_id>/scores', methods=['GET'])
@jwt_required()
@admin_required
def get_user_scores(user_id):
    scores = Score.query.filter_by(user_id=user_id).all()
    output = []
    for score in scores:
        score_data = {
            'quiz_title': score.quiz.title,
            'score': score.score,
            'timestamp': score.timestamp
        }
        output.append(score_data)
    return jsonify({'scores': output})

@admin_bp.route('/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully!'})

@admin_bp.route('/users/<int:user_id>', methods=['PUT'])
@jwt_required()
@admin_required
def update_user(user_id):
    data = request.get_json()
    user = User.query.get_or_404(user_id)
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    user.role = data.get('role', user.role)
    db.session.commit()
    return jsonify({'message': 'User updated successfully!'})