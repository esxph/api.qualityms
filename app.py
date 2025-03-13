import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Set database connection from .env
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Routes
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(email=data['email'], password_hash=data['password_hash'], full_name=data.get('full_name'), phone=data.get('phone'))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully!"}), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{"user_id": user.user_id, "email": user.email, "full_name": user.full_name} for user in users])

@app.route('/')
def home():
    return "Flask API with MySQL (qualityms) and Docker is running"
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
