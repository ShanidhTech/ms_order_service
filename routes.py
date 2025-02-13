from flask import Blueprint, request, jsonify
from .models import Order  # Import the Order model
from . import db  # Import the db instance

order_bp = Blueprint('orders', __name__, url_prefix='/orders')

@order_bp.route("/", methods=["POST"])
def create_order():
    try:
        order_data = request.get_json()
        new_order = Order(
            book_id=order_data['book_id'],  # Get data from JSON
            quantity=order_data['quantity'],
            user_id=order_data['user_id'],
        )

        db.session.add(new_order)
        db.session.commit()

        return jsonify({"message": "Order created", "order": new_order.__dict__}), 201  # Convert to dict for JSON

    except Exception as e:
        db.session.rollback()  # Important: Rollback on error
        return jsonify({"error": str(e)}), 500  # Return error message

@order_bp.route("/", methods=["GET"])
def get_orders():
    orders = Order.query.all()
    order_list = []
    for order in orders:
        order_list.append(order.__dict__)
    return jsonify(order_list), 200
