# app/controllers/category_controller.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models.category_model import Category
from app import db
from decorators import admin_required

category_bp = Blueprint('category', __name__)

@category_bp.route('/categories', methods=['POST'])
@jwt_required()
@admin_required
def create_category():
    data = request.get_json()
    new_category = Category(name=data['name'])
    db.session.add(new_category)
    db.session.commit()
    return jsonify({'message': 'Category created successfully!'})

@category_bp.route('/categories', methods=['GET'])
@jwt_required()
def get_categories():
    categories = Category.query.all()
    output = [{'id': category.id, 'name': category.name} for category in categories]
    return jsonify({'categories': output})

@category_bp.route('/categories/<int:category_id>', methods=['PUT'])
@jwt_required()
@admin_required
def edit_category(category_id):
    data = request.get_json()
    category = Category.query.get_or_404(category_id)
    category.name = data.get('name', category.name)
    db.session.commit()
    return jsonify({'message': 'Category updated successfully!'})

@category_bp.route('/categories/<int:category_id>', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return jsonify({'message': 'Category deleted successfully!'})
