from kafka import KafkaConsumer
import json, os

consumer = KafkaConsumer(
    'order_topic',
    bootstrap_servers=os.environ.get('KAFKA_BOOTSTRAP','localhost:9092'),
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    order = message.value
    print(f"Order Event Received: {order.get('user_id')} ordered from {order.get('restaurant_id')}")
