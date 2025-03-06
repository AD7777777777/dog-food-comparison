from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)  # Enables CORS for all domains

@app.route('/compare', methods=['POST'])
def compare():
    data = request.json
    dog_size = data.get("size")
    weight = data.get("weight")
    age = data.get("age")

    # Dummy response for testing
    brands = [
        {"brand": "Brand A", "ingredients": "Chicken, Rice, Carrots"},
        {"brand": "Brand B", "ingredients": "Beef, Oats, Peas"},
        {"brand": "Brand C", "ingredients": "Salmon, Sweet Potato, Flaxseed"},
    ]

    response = jsonify(brands)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

print("Available routes:")
for rule in app.url_map.iter_rules():
    print(rule)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
