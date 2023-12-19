from flask import Blueprint, request, jsonify
from models.user_model import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

# Create a Blueprint instance for user-related routes
blueprint1 = Blueprint("Register_users", __name__)

@blueprint1.route("/register", methods=["POST"])
def register():
    """Registers a new user with the provided details.

    Receives user data in JSON format and creates a new User object
    in the database. Returns a success message on successful registration.

    Args:
        data (dict): JSON data containing user information,
        including first_name, last_name, gender, date_of_birth,
        phone_number, email, address, country_of_origin, and password.

    Returns:
        JSON: message indicating successful registration.
    """
    data = request.get_json()
    first_name = data["first_name"]
    last_name = data["last_name"]
    gender = data["gender"]
    date_of_birth = data["date_of_birth"]
    phone_number = data["phone_number"]
    email = data["email"]
    address = data["address"]
    country_of_origin = data["country_of_origin"]
    password = data["password"]

    # Hash the password using bcrypt
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Create a new User object and populate its attributes
    user = User()
    user.first_name = first_name
    user.last_name = last_name
    user.gender = gender
    user.date_of_birth = date_of_birth
    user.phone_number = phone_number
    user.email = email
    user.address = address
    user.country_of_origin = country_of_origin
    user.password = hashed_password
    # Save the user to the database
    user.save()

    # Return a success message
    return jsonify(message='Registration successful'), 201
