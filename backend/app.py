from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from faker import Faker
import random

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS to allow frontend requests

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }

# Seed the database with 100 mock products
def setup_database():
    with app.app_context():
        db.create_all()

        if Product.query.count() == 0:
            fake = Faker()
            products = []

            for _ in range(100):
                name = fake.unique.word().capitalize() + " " + fake.word().capitalize()
                price = random.randint(500, 5000)
                stock = random.randint(5, 50)
                products.append(Product(name=name, price=price, stock=stock))

            db.session.add_all(products)
            db.session.commit()
            print("✅ Database initialized with 100 mock products.")

# Home route (optional)
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Sales Chatbot API"})

# GET /products — Return all products
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([p.to_dict() for p in products])

# POST /add-product — Add a new product to the database
@app.route('/add-product', methods=['POST'])
def add_product():
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 400

    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    stock = data.get('stock')

    # Basic validation
    if not name:
        return jsonify({"error": "Product name is required"}), 400
    if not isinstance(price, int) or not isinstance(stock, int):
        return jsonify({"error": "Price and stock must be integers"}), 400

    # Save new product to DB
    new_product = Product(name=name, price=price, stock=stock)
    db.session.add(new_product)
    db.session.commit()

    return jsonify({"message": f"Product '{name}' added successfully!"}), 201

# Start server
if __name__ == '__main__':
    setup_database()
    app.run(debug=True)
