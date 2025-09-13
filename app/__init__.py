import os
from flask import Flask, g
from .app_factory import create_app
from .db_connect import close_db, get_db

app = create_app()
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-for-development')

# Register Blueprints
from app.blueprints.examples import examples

app.register_blueprint(examples, url_prefix='/example')

from . import routes

@app.before_request
def before_request():
    try:
        g.db = get_db()
    except Exception as e:
        g.db = None
        print(f"Warning: Database connection unavailable: {e}. Some features may not work.")

# Setup database connection teardown
@app.teardown_appcontext
def teardown_db(exception=None):
    close_db(exception)