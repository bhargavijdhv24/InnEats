import bcrypt
import os
from datetime import datetime, timedelta
import jwt

SECRET_KEY = os.environ.get("SECRET_KEY", "inneatssecret")

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

def generate_jwt(payload, exp_minutes=60):
    payload['exp'] = datetime.utcnow() + timedelta(minutes=exp_minutes)
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def decode_jwt(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except Exception:
        return None
