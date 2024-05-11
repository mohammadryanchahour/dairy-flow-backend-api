from flask import Blueprint, json, request
from helpers.custom_responses import success_response, error_response
from middlewares.validators import validate_delivery
from services.delivery_services import create_bulk_deliveries, create_delivery, get_all_deliveries, get_delivery_by_id, update_delivery

delivery_routes = Blueprint('delivery_routes', __name__)

@delivery_routes.route('/create-delivery', methods=['POST'])
@validate_delivery
def create(validated_payload):
    try:
        delivery, error = create_delivery(validated_payload)

        if error:
            return error

        delivery = json.loads(delivery.to_json())

        return success_response(delivery, "Delivery Created Successfully", 201)
    
    except Exception as e:
        return error_response(f"Internal Server Error => {str(e)}", 500)
    
@delivery_routes.route('/create-bulk-delivery', methods=['POST'])
def create_bulk():
    try:
        payloads = request.json if request.headers.get('Content-Type') == 'application/json' else request.form

        if not isinstance(payloads, list):
            return error_response("Invalid payload format. Expected a list of deliveries.", 400)
        
        deliveries, error = create_bulk_deliveries(payloads)

        if error:
            return error

        deliveries = [json.loads(delivery.to_json()) for delivery in deliveries]

        return success_response(deliveries, "Bulk Deliveries Created Successfully", 201)
    
    except Exception as e:
        return error_response(f"Internal Server Error => {str(e)}", 500)
    
@delivery_routes.route('/get-all-deliveries', methods=['GET'])
def get_deliveries():
    try:
        deliveries, error = get_all_deliveries()

        if error:
            return error
        
        deliveries = json.loads(deliveries.to_json())

        return success_response(deliveries, "All Deliveries Retrieved Successfully", 200)
    
    except Exception as e:
        return error_response(f"Internal Server Error => {str(e)}", 500)
    
@delivery_routes.route('/get-delivery/<string:delivery_id>', methods=['GET'])
def get_delivery(delivery_id):
    try:
        delivery, error = get_delivery_by_id(delivery_id)

        if error:
            return error
        
        delivery = json.loads(delivery.to_json())

        return success_response(delivery, "Delivery Retrieved Successfully", 200)
    
    except Exception as e:
        return error_response(f"Internal Server Error => {str(e)}", 500)
    
@delivery_routes.route('/update-delivery/<string:delivery_id>', methods=['PATCH'])
def update(delivery_id):
    try:
        payload = request.json if request.headers.get('Content-Type') == 'application/json' else request.form
        updated_delivery, error = update_delivery(delivery_id, payload)

        if error:
            return error

        updated_delivery = json.loads(updated_delivery.to_json())

        return success_response(updated_delivery, "Delivery Updated Successfully", 200)
    
    except Exception as e:
        return error_response(f"Internal Server Error => {str(e)}", 500)
    
@delivery_routes.route('/delete-delivery/<string:delivery_id>', methods=['DELETE'])
def delete_delivery(delivery_id):
    try:
        delivery, error = get_delivery_by_id(delivery_id)

        if error:
            return error

        delivery.delete()

        return success_response("Delivery Deleted Successfully", 200)
    
    except Exception as e:
        return error_response(f"Internal Server Error => {str(e)}", 500)
