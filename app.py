import os
import mysql.connector
from flask import Flask, jsonify
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

app = Flask(__name__)

# Set database connection from .env
app.config['DB_HOST'] = os.getenv("MYSQL_HOST")
app.config['DB_USER'] = os.getenv("MYSQL_USER")
app.config['DB_PASSWORD'] = os.getenv("MYSQL_PASSWORD")
app.config['DB_NAME'] = os.getenv("MYSQL_DATABASE")


def get_db_connection():
    """
    Create and return a new database connection using mysql-connector-python.
    In production, you might want to use a connection pool instead of creating a new connection each time.
    """
    return mysql.connector.connect(
        host=app.config['DB_HOST'],
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD'],
        database=app.config['DB_NAME']
    )

'''# Routes
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
'''
@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({"status": "ok"}), 200

@app.route('/get-users', methods=['GET'])
def get_users():
    try:
        connection = get_db_connection()
        cursos = connection.cursor(dictionary=True)
        query = "SELECT * FROM Users;"
        cursor.execute("SELECT * FROM Users")
        query_result = cursor.fetchall()

        #Closes the current connection and clears the cursor
        cursor.close()
        connection.close()
        
        return jsonify(query_result), 200

    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
