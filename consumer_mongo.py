from kafka import KafkaConsumer
from pymongo import MongoClient
import json

consumer = KafkaConsumer(
    "transactions",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["stripe"]
collection = db["transactions"]

print("Saving Kafka transactions to MongoDB...")

for message in consumer:

    transaction = message.value
    print("Received:", transaction)

    collection.insert_one(transaction)