from flask import Flask, request, jsonify
from common.db import db
from kafka import KafkaProducer
import json, os

app = Flask(__name__)
restaurants_collection = db["restaurants"]
orders_collection = db["orders"]

producer = KafkaProducer(bootstrap_servers=os.environ.get('KAFKA_BOOTSTRAP','localhost:9092'), value_serializer=lambda v: json.dumps(v).encode('utf-8'))

@app.route("/menu/<restaurant_id>", methods=["GET"])
def menu(restaurant_id):
    restaurant = restaurants_collection.find_one({"id": restaurant_id})
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    return jsonify(restaurant.get('menu', [])), 200

@app.route("/order", methods=["POST"])
def place_order():
    data = request.json
    orders_collection.insert_one(data)
    try:
        producer.send('order_topic', data)
    except Exception as e:
        print("Kafka send error:", e)
    return jsonify({"message": "Order placed successfully"}), 201

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host='0.0.0.0', port=port, debug=True)
