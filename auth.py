import jwt
import datetime
import os
from flask import request, jsonify
from dotenv import load_dotenv

load_dotenv()
JWT_SECRET = os.getenv("JWT_SECRET")

USERS = {"teste@teste.com": "teste@teste.com"}


def generate_token(email):
    payload = {
        "email": email,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=6),
    }
    return jwt.encode(payload, JWT_SECRET, algorithm="HS256")


def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if USERS.get(email) == password:
        token = generate_token(email)
        return jsonify({"token": token}), 200
    else:
        return jsonify({"error": "Credenciais inválidas"}), 401


def verify_token(func):
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return jsonify({"error": "Token ausente"}), 401
        token = auth_header.split(" ")[1]
        try:
            jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expirado"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Token inválido"}), 401
        return func(*args, **kwargs)

    wrapper.__name__ = func.__name__
    return wrapper
