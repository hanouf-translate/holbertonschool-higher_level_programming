#!/usr/bin/python3
"""
Module that implements a simple RESTful API using the Flask framework.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory dictionary to store users
users = {}


@app.route('/')
def home():
    """
    Root endpoint that returns a welcome message.
    """
    return "Welcome to the Flask API!"


@app.route('/status')
def status():
    """
    Status endpoint that returns OK.
    """
    return "OK"


@app.route('/data')
def get_data():
    """
    Returns a JSON list of all stored usernames.
    """
    return jsonify(list(users.keys()))


@app.route('/users/<username>')
def get_user(username):
    """
    Returns the user details corresponding to the provided username.
    Returns 404 if the user does not exist.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Adds a new user to the in-memory dictionary via a POST request.
    Validates JSON content, presence of username, and uniqueness.
    """
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add user to dictionary
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run()