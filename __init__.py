from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Initialize SQLAlchemy (but don't bind to an app yet)

from . import models  # Import your models