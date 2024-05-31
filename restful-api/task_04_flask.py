#!/usr/bin/python3
"""
    Route flask API.
"""
from flask import Flask, jsonify, request
import json


app = Flask(__name__)
users = {}


@app.route('/')
def hello():
    """
        Root route of the Flask API.

        Returns:
            str: Welcome message.
    """
    return 'Welcome to the Flask API!'


@app.route('/data')
def data():
    """
        Retrieve list of usernames.

        Returns:
            List of usernames.
    """
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """
        Retrieve the status of the API.

        Returns:
            str: Message "OK".
    """
    return "OK"


@app.route('/users/<username>')
def user(username):
    """
        Retrieve user information based from the username.

        Args:
            username: Username to retrieve.

        Returns:
            Data of the user.

            If not exist, error 404.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
        Add a user to the API.

        Returns:
            Data of the new user, with message of confirmation.

            If error, error message with error 400.
    """
    new_user = request.get_json()
    username = new_user.get("username")
    if not username:
        return jsonify({"error": "Username required"}), 400
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = {
        "username": username,
        "name": new_user.get("name"),
        "age": new_user.get("age"),
        "city": new_user.get("city")
    }
    return jsonify({
        "message": "User added",
        "user": new_user
    }), 201


if __name__ == "__main__":
    app.run()
