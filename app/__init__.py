from flask import Flask
from .database import init_db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flashcards.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize database
    init_db(app)

    # Import and register routes
    from .routes import bp
    app.register_blueprint(bp)

    return app
