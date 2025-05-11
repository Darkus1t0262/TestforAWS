from flask import Flask, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)
mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(mongo_uri)
db = client["mydb"]
collection = db["items"]

@app.route('/api/items', methods=['GET'])
def get_items():
    items = list(collection.find({}, {"_id": 0}))
    return jsonify(items)

@app.route('/api/items/add/<item>', methods=['GET'])
def add_item(item):
    collection.insert_one({"item": item})
    return jsonify({"message": f"Item '{item}' added!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
