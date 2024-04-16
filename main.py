# Import necessary libraries
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

# Initialize Flask app
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///requests.db'
db = SQLAlchemy(app)

# Define a model for storing requests and responses
class RequestResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cadastre_number = db.Column(db.String(20))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    external_response = db.Column(db.Boolean)

@app.route('/')
def main():
    return render_template('base.html')

# Define endpoints
@app.route('/query', methods=['POST'])
def receive_query():
    # Code to handle incoming query
    pass

@app.route('/result', methods=['POST'])
def send_result():
    # Code to send the result
    pass

@app.route('/ping')
def ping_server():

    return 'Server is running'

@app.route('/history')
def get_history():
    # Code to retrieve history of requests
    pass

# Add Admin interface
admin = Admin(app, name='Admin Panel', template_mode='bootstrap3')

# Wrap the service in a Dockerfile (not shown in code snippet)

if __name__ == '__main__':
    app.run(debug=True)