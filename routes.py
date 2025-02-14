from flask import Blueprint, request, jsonify
from .models import Order  # Import the Order model
from . import db  # Import the db instance

order_bp = Blueprint('orders', __name__, url_prefix='/orders')

@order_bp.route("/", methods=["POST"])
def create_order():
    try:
        order_data = request.get_json()
        new_order = Order(
            book_id=order_data['book_id'],
            quantity=order_data['quantity'],
            user_id=order_data['user_id'],
            total_amount=order_data['total_amount'],
            shipping_address=order_data['shipping_address']
        )

        db.session.add(new_order)
        db.session.commit()

        # Return formatted order data instead of __dict__
        response_data = {
            "message": "Order created",
            "order": {
                'id': new_order.id,
                'book_id': new_order.book_id,
                'quantity': new_order.quantity,
                'user_id': new_order.user_id,
                'total_amount': new_order.total_amount,
                'shipping_address': new_order.shipping_address
            }
        }
        return jsonify(response_data), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@order_bp.route("/", methods=["GET"])
def get_orders():
    orders = Order.query.all()
    order_list = []
    for order in orders:
        order_list.append({
            'id': order.id,
            'book_id': order.book_id,
            'quantity': order.quantity,
            'user_id': order.user_id,
            'total_amount': order.total_amount,
            'shipping_address': order.shipping_address
        })
    return jsonify(order_list), 200
