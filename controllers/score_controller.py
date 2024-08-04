from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.score_model import Score
from app import db

score_bp = Blueprint('score', __name__)

@score_bp.route('/quizzes/<quiz_id>/scores', methods=['POST'])
@jwt_required()
def submit_score(quiz_id):
    data = request.get_json()
    current_user_id = get_jwt_identity()
    new_score = Score(
        user_id=current_user_id,
        quiz_id=quiz_id,
        score=data['score']
    )
    db.session.add(new_score)
    db.session.commit()
    return jsonify({'message': 'Score submitted successfully!'})

@score_bp.route('/scores', methods=['GET'])
@jwt_required()
def get_scores():
    current_user_id = get_jwt_identity()
    scores = Score.query.filter_by(user_id=current_user_id).all()
    output = []
    for score in scores:
        score_data = {
            'quiz_title': score.quiz.title,
            'score': score.score,
            'timestamp': score.timestamp
        }
        output.append(score_data)
    return jsonify({'scores': output})
