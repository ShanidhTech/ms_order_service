# main.py (or app.py - choose a consistent name)
from flask import Flask
from . import config  # Import configuration
from . import db  # Import the db instance (after initializing it)
from .routes import order_bp  # Import the order blueprint
from flask_migrate import Migrate

app = Flask(__name__)

# Load configuration
app.config.from_object(config)

# Initialize SQLAlchemy
db.init_app(app)  # Initialize db with the app

# Register Blueprints
app.register_blueprint(order_bp)

# Create tables (run this ONCE to create the database schema)
with app.app_context():
    db.create_all()

migrate = Migrate(app, db)    

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8002, debug=True)  # debug=True for development