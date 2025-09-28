from flask import Flask, request, jsonify
from common.db import db
from common.utils import hash_password, check_password, generate_jwt
from bson import ObjectId
import os

app = Flask(__name__)
users_collection = db["users"]

@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    if users_collection.find_one({"email": data.get('email')}):
        return jsonify({"error": "Email already exists"}), 400
    data['password'] = hash_password(data.get('password', ''))
    users_collection.insert_one({"email": data.get('email'), "password": data['password'], "name": data.get('name', '')})
    return jsonify({"message": "User created successfully"}), 201

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    user = users_collection.find_one({"email": data.get('email')})
    if not user or not check_password(data.get('password',''), user['password']):
        return jsonify({"error": "Invalid credentials"}), 401
    token = generate_jwt({"user_id": str(user['_id'])})
    return jsonify({"token": token}), 200

@app.route("/profile/<user_id>", methods=["GET"])
def profile(user_id):
    user = users_collection.find_one({"_id": ObjectId(user_id)}, {"password": 0})
    if not user:
        return jsonify({"error": "User not found"}), 404
    user['id'] = str(user['_id'])
    user.pop('_id', None)
    return jsonify(user), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
