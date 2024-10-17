from flask import Flask, jsonify
from decimal import Decimal
import json

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Kitchen View!"

# Custom JSON Encoder for Decimal types
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)  # Convert Decimal to float
        return super().default(obj)

# Set the custom JSON encoder for the app
app.json_encoder = DecimalEncoder

# Sample data for menu
menu = [
    {"id": 1, "name": "Cheeseburger", "price": Decimal('5.99')},
    {"id": 2, "name": "Veggie Burger", "price": Decimal('4.99')},
    {"id": 3, "name": "Chicken Burger", "price": Decimal('6.49')}
]

@app.route('/menu', methods=['GET'])
def get_menu():
    return jsonify(menu)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
