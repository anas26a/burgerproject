from flask import Flask, jsonify, render_template
import decimal

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('/index')

# Custom JSON Encoder to handle Decimal types
class CustomJSONEncoder(jsonify.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)  # Convert Decimal to float
        return super().default(obj)

app.json_encoder = CustomJSONEncoder

# Mock database retrieval function
def get_menu_from_db():
    # Example menu with Decimal values
    return [
        {"name": "Cheeseburger", "price": decimal.Decimal('9.99'), "description": "A delicious cheeseburger."},
        {"name": "Veggie Burger", "price": decimal.Decimal('8.49'), "description": "A tasty veggie option."},
        {"name": "Bacon Burger", "price": decimal.Decimal('10.99'), "description": "A burger with crispy bacon."}
    ]

@app.route('/menu', methods=['GET'])
def get_menu():
    menu = get_menu_from_db()  # Get menu from the database (mocked here)
    return jsonify(menu)  # Use jsonify to return the response

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Burger Orderer!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Allow access from other machines
