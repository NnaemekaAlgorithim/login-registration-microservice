from flask import Flask
from Flask_files.Registration import blueprint1
from Flask_files.Login import blueprint2
from flask_jwt_extended import JWTManager
import secrets

# Create a Flask app
app = Flask(__name__)

secret_key = secrets.token_hex(16)
app.config['JWT_SECRET_KEY'] = secret_key
jwt = JWTManager(app)

# Register the blueprint with the app
app.register_blueprint(blueprint1)
app.register_blueprint(blueprint2)

if __name__ == '__main__':
    app.run()
