from flask import Blueprint
from flask import request, jsonify
from models.user_model import User
from flask_jwt_extended import create_access_token


# Create a Blueprint instance
blueprint2 = Blueprint('Login_users', __name__)

@blueprint2.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Validate inputs
    if not email or not password:
        return jsonify({'error': 'Email and password are required.'}), 400

    # Retrieve user from the database
    user = User.check_user(email, password)

    if user:
        # Successful login
        access_token = create_access_token(identity = user.user_id)
        response = jsonify({'message': 'Login successful.', 'access_token': access_token})
        return response, 200
    else:
        # Invalid credentials
        return jsonify({'error': 'Invalid email or password.'}), 401
