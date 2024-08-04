from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, request, jsonify, redirect, url_for, render_template
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app import db
from models.user_model import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    role = data.get('role', 'user')  # Default role is 'user'
    new_user = User(username=data['username'], email=data['email'], password=hashed_password, role=role)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully!'})

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # Render the login page
        return render_template('login.html')

    # Handle POST request
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Find user by username
    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({'msg': 'Invalid credentials'}), 401

    # Create access token
    access_token = create_access_token(identity={'id': user.id, 'role': user.role})
    return jsonify({'access_token': access_token})
