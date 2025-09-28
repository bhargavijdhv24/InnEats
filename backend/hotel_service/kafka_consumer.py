from kafka import KafkaConsumer
import json, os
from common.db import db

consumer = KafkaConsumer(
    'booking_topic',
    bootstrap_servers=os.environ.get('KAFKA_BOOTSTRAP','localhost:9092'),
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    booking = message.value
    print(f"Booking Event Received: {booking.get('user_id')} booked {booking.get('hotel_id')}")
    # update DB availability logic could go here
