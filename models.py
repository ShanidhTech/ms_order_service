from . import db  # Import the db instance

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # product = db.Column(db.String(80), nullable=False)
    book_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return f'<Order {self.product} x {self.quantity}>'