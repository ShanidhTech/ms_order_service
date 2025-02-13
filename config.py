import os

# Database Configuration (PostgreSQL example)
DB_USER = os.environ.get("DB_USER") or "postgres"
DB_PASSWORD = os.environ.get("DB_PASSWORD") or "password"
DB_HOST = os.environ.get("DB_HOST") or "localhost"
DB_NAME = os.environ.get("DB_NAME") or "order_bookstore"

SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False