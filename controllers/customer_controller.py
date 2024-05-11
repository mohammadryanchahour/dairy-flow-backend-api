from flask import Blueprint, json, request
from middlewares.validators import validate_customer
from helpers.custom_responses import success_response, error_response
from services.customer_services import create_customer, get_all_customers, get_customer_by_id, get_filtered_customers, update_customer, update_customer_position

customer_routes = Blueprint('customer_routes', __name__)

@customer_routes.route('/create-customer', methods=['POST'])
@validate_customer
def create(validated_payload):
    try:
        customer, error = create_customer(validated_payload)

        if error:
            return error
        
        customer = json.loads(customer.to_json())

        return success_response(customer,"Customer Created Successfully", 201)
    
    except Exception as e:
        return error_response(f"Internal Server Error => {str(e)}", 500)

@customer_routes.route('/get-all-customers', methods=['GET'])
def get_customers():
    try:
        customers, error = get_all_customers()

        if error:
            return error
        
        customers = json.loads(customers.to_json())

        return success_response(customers, "Customers Retrieved Successfully", 200)
    
    except Exception as e:
        return error_response(f"Internal Server Error => {str(e)}", 500)

@customer_routes.route('/get-customer/<string:customer_id>', methods=["GET"])
def get_customer(customer_id):
    try:
        customer, error = get_customer_by_id(customer_id)

        if error:
            return error
        
        customer = json.loads(customer.to_json())

        return success_response(customer, "Customer Retrieved Successfully", 200)
    
    except Exception as e:
        return error_response(f"Internal Server Error => {str(e)}", 500)
    
@customer_routes.route("/update-customer/<string:customer_id>", methods=["PATCH"])
def update(customer_id):
    try:
        payload = request.json if request.headers.get('Content-Type') == 'application/json' else request.form

        updated_customer, error = update_customer(customer_id, payload)
        if error:
            return error
        
        return success_response(updated_customer, "Customer Updated Successfully", 200)
    
    except Exception as e:
        return error_response(f"Internal Server Error => {str(e)}", 500)

@customer_routes.route("update-position/<string:customer_id>", methods=["PATCH"])
def update_position(customer_id):
    try:
        payload = request.json if request.headers.get('Content-Type') == 'application/json' else request.form

        new_position = payload["position"]
        
        # Update the existing customer with the validated payload
        updated_customer, error = update_customer_position(customer_id, new_position)

        if error:
            return error
        
        return success_response(json.loads(updated_customer.to_json()), "Customer Updated Successfully", 200)
    
    except Exception as e:
        return error_response(f"Internal Server Error => {str(e)}", 500)
    
@customer_routes.route("/delete-customer/<string:customer_id>", methods=["DELETE"])
def delete(customer_id):
    try:
        customer, error = get_customer_by_id(customer_id)

        if error:
            return error
        
        customer.delete()

        return success_response(None, "Customer Deleted Successfully", 200)
    
    except Exception as e:
        return error_response(f"Internal Server Error => {str(e)}", 500)
    
@customer_routes.route("filter-customers", methods=["POST"])
def filter():
    try:
        payload = request.json if request.headers.get('Content-Type') == 'application/json' else request.form

        search_filters = payload.get('search_filters', {})

        customers, error = get_filtered_customers(search_filters)

        if error:
            return error
        
        customers = json.loads(customers.to_json())

        return success_response(customers, "Customers Retrieved Successfully", 200)
    
    except Exception as e:
        return error_response(f"Internal Server Error => {str(e)}", 500)