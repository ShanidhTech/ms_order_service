from flask import Flask, request, jsonify

app = Flask(__name__)

orders = []

@app.route("/orders/", methods=["POST"])
def create_order():
    order = request.json
    orders.append(order)
    return jsonify({"message": "Order created", "order": order}), 201

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8002)
