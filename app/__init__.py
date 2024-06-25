from flask import Flask
from datetime import timedelta

def create_app():
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.permanent_session_lifetime = timedelta(days=7)
    from .routes.app import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app
