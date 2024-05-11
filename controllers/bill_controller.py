from flask import Blueprint, json
from helpers.custom_responses import error_response, success_response
from services.bill_services import generate_bills

# Create a Blueprint for bill_controller
bill_routes = Blueprint('bill_routes', __name__)

# Endpoint to generate a bill
@bill_routes.route('/generate-bill', methods=['POST'])
def generate():
    try:
        bills, error = generate_bills()

        if error:
            return error
        
        bills = [json.loads(bill.to_json()) for bill in bills]

        return success_response(bills,"Bill Generated Successfully", 201)
    
    except Exception as e:
        return error_response(f"Internal Server Error => {str(e)}", 500)
