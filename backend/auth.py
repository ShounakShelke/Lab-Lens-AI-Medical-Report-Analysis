from flask import Blueprint, request, jsonify
import os
import uuid
from database import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth/signup', methods=['POST'])
def signup():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    name = data.get('name', 'User')

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    if db.get_user_by_email(email):
        return jsonify({"error": "User already exists"}), 400

    new_user = {
        "id": str(uuid.uuid4()),
        "email": email,
        "password": password,
        "name": name,
        "auth_type": "credentials",
        "avatar": f"https://api.dicebear.com/7.x/initials/svg?seed={name}"
    }
    
    db.save_user(new_user)
    
    return jsonify({"success": True, "user": new_user, "token": "mock-jwt-token"}), 201

@auth_bp.route('/auth/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = db.get_user_by_email(email)

    if user and user.get('password') == password:
         return jsonify({"success": True, "user": user, "token": "mock-jwt-token"}), 200
    
    return jsonify({"error": "Invalid credentials"}), 401

@auth_bp.route('/auth/save-user', methods=['POST'])
def save_user():
    data = request.json
    try:
        email = data.get('email')
        existing_user = db.get_user_by_email(email)

        if not existing_user:
            data['auth_type'] = 'google'
            db.save_user(data)
            
        return jsonify({"status": "User saved/updated"}), 200
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@auth_bp.route('/auth/google', methods=['POST'])
def google_login():
    data = request.json
    credential = data.get('credential')

    # Demo logic preserved
    email = "visitor@lablens.demo" 
    name = "Visitor User"
    role = "user"

    if credential == "demo-token-admin":
        email = "admin@lablens.demo"
        name = "Dr. Admin"
        role = "medperson"
        
    existing_user = db.get_user_by_email(email)
    
    if not existing_user:
        existing_user = {
            "id": str(uuid.uuid4()),
            "email": email,
            "name": name,
            "auth_type": "google",
            "avatar": f"https://api.dicebear.com/7.x/initials/svg?seed={name}",
            "role": role 
        }
        db.save_user(existing_user)
    else:
        if existing_user.get('role') != role:
            existing_user['role'] = role
            db.save_user(existing_user)
        
    return jsonify({
        "success": True, 
        "user": existing_user, 
        "token": "mock-jwt-token"
    }), 200

@auth_bp.route('/auth/logout', methods=['POST'])
def logout():
    return jsonify({"success": True}), 200

@auth_bp.route('/auth/user', methods=['GET'])
def get_current_user():
    return jsonify({"error": "Not implemented"}), 501
