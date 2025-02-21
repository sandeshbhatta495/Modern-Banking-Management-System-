from flask import Blueprint, jsonify, request
from database.db import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return jsonify({"message": "Login endpoint", "status": "success"})

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    return jsonify({"message": "Register endpoint", "status": "success"})

@auth_bp.route('/logout', methods=['POST'])
def logout():
    return jsonify({"message": "Logged out successfully"})
