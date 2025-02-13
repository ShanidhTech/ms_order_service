from datetime import datetime 
from sqlalchemy import DateTime, Numeric
from . import db  # Import the db instance
import enum
from sqlalchemy import Enum

class OrderStatus(enum.Enum):
    PENDING = 1
    PROCESSING = 2
    SHIPPED = 3
    DELIVERED = 4
    CANCELLED = 5

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # product = db.Column(db.String(80), nullable=False)
    book_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    order_date = db.Column(DateTime, default=datetime.utcnow)
    total_amount = db.Column(Numeric(10, 2), nullable=False)
    shipping_address = db.Column(db.String(300), nullable=False)
    # status = db.Column(db.Integer, nullable=False)
    status = db.Column(Enum(OrderStatus), nullable=False)



    def __repr__(self):
        return f'<Order {self.product} x {self.quantity}>'