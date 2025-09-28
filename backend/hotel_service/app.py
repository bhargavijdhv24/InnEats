from flask import Flask, request, jsonify
from common.db import db
from kafka import KafkaProducer
import json, os

app = Flask(__name__)
hotels_collection = db["hotels"]
bookings_collection = db["bookings"]

producer = KafkaProducer(bootstrap_servers=os.environ.get('KAFKA_BOOTSTRAP','localhost:9092'), value_serializer=lambda v: json.dumps(v).encode('utf-8'))

@app.route("/hotels", methods=["GET"])
def list_hotels():
    hotels = []
    for h in hotels_collection.find({}):
        h['id'] = str(h.get('_id'))
        h.pop('_id', None)
        hotels.append(h)
    return jsonify(hotels), 200

@app.route("/book", methods=["POST"])
def book_room():
    data = request.json
    bookings_collection.insert_one(data)
    try:
        producer.send('booking_topic', data)
    except Exception as e:
        print("Kafka send error:", e)
    return jsonify({"message": "Room booked successfully"}), 201

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port, debug=True)
