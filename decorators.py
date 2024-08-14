from functools import wraps
from flask_jwt_extended import get_jwt_identity
from flask import jsonify, request
from models.user_model import User

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            identity = get_jwt_identity()
            
            user_id = identity.get('id') if isinstance(identity, dict) else identity
            user = User.query.get(user_id)

            if user and user.role == 'admin':
                return fn(*args, **kwargs)
            else:
                return jsonify({'message': 'Admins only!'}), 403
        except Exception as e:
            print(f"Error in admin_required decorator: {e}")
            return jsonify({'message': 'Authorization error!'}), 403
        


    return wrapper
