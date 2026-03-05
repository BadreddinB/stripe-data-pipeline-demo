from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

print("Sending Stripe transactions to Kafka...")

while True:

    transaction = {
        "transaction_id": random.randint(1000,9999),
        "customer_id": random.randint(1,100),
        "amount": round(random.uniform(10,500),2),
        "currency": "USD",
        "fraud_score": round(random.uniform(0,1),2)
    }

    producer.send("transactions", transaction)

    print("Sent:", transaction)

    time.sleep(2)