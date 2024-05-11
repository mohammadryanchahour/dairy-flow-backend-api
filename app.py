import os
from flask import Flask, jsonify
from controllers.customer_controller import customer_routes
from controllers.delivery_controller import delivery_routes
from controllers.bill_controller import bill_routes
from mongoengine import connect

mongo_uri = os.getenv("MONGO_DB_URI")

app = Flask(__name__)

connect(host=mongo_uri)

# Routes Registration
app.register_blueprint(customer_routes, url_prefix="/api")
app.register_blueprint(delivery_routes, url_prefix="/api")
app.register_blueprint(bill_routes, url_prefix="/api")

@app.route('/health')
def health_check():
    try:
        
        db = connect(host=mongo_uri)  
        db.command({"ping": 1})
        return jsonify({'status': 'OK', 'db_status': 'connected'})
    except Exception as e:
        return jsonify({'status': 'ERROR', 'message': f"Error accessing MongoDB: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True, port=3000)
