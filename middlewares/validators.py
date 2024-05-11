from functools import wraps
import re
from flask import request
from helpers.custom_responses import error_response

def validate_customer(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            payload = request.json if request.headers.get('Content-Type') == 'application/json' else request.form
                
            required_fields = ['name', 'phone', 'rate_id']
                
            missing_fields = [field for field in required_fields if field not in payload]
            if missing_fields:
                return error_response(f"{missing_fields} are required", 400)
            
            if "name" in payload and not re.match(r'^[A-Za-z\s]+$', payload["name"]):
                return error_response("Invalid Name Format. Only Alphabets & Spaces are allowed", 400)
            
            if "phone" in payload and not re.match(r'^03\d{2}-\d{7}$', payload["phone"]):
                return error_response("Invalid Phone Format. It should be in 03XX-XXXXXXX", 400)
            
            if "address" in payload:
                address = payload["address"]
                if not isinstance(address, str) or not address.strip():
                    return error_response("Invalid Address Format. It should be a non-empty string.", 400)
                
            if "rate_id" in payload:
                rate_id = payload["rate_id"]
                if not isinstance(rate_id, str) or not rate_id.strip() or not len(rate_id) == 24:
                    return error_response("Invalid Rate ID Format. It should be a non-empty string.", 400)
                
        except Exception as e:
            return error_response(f"Internal Server Error => {str(e)}", 500)

        return f(payload, *args, **kwargs)
    return wrapper

def validate_update_customer(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            payload = request.json if request.headers.get('Content-Type') == 'application/json' else request.form

            allowed_fields = ['name', 'phone', 'address', 'rate_id']

            if not payload:
                return error_response("No data provided for update", 400)

            invalid_fields = [field for field in payload if field not in allowed_fields]
            if invalid_fields:
                return error_response(f"Invalid fields provided: {invalid_fields}", 400)

            if "name" in payload and not re.match(r'^[A-Za-z\s]+$', payload["name"]):
                return error_response("Invalid Name Format. Only Alphabets & Spaces are allowed", 400)

            if "phone" in payload and not re.match(r'^03\d{2}-\d{7}$', payload["phone"]):
                return error_response("Invalid Phone Format. It should be in 03XX-XXXXXXX", 400)

            if "address" in payload:
                address = payload["address"]
                if not isinstance(address, str) or not address.strip():
                    return error_response("Invalid Address Format. It should be a non-empty string.", 400)

            if "rate_id" in payload:
                rate_id = payload["rate_id"]
                if not isinstance(rate_id, str) or not rate_id.strip() or not len(rate_id) == 24:
                    return error_response("Invalid Rate ID Format. It should be a non-empty string.", 400)

        except Exception as e:
            return error_response(f"Internal Server Error => {str(e)}", 500)

        return f(payload, *args, **kwargs)

    return wrapper

def validate_delivery(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            payload = request.json if request.headers.get('Content-Type') == 'application/json' else request.form

            required_fields = ['delivery_quantity', 'delivery_date', 'customer_id']

            missing_fields = [field for field in required_fields if field not in payload]
            if missing_fields:
                return error_response(f"{missing_fields} are required", 400)
            
            delivery_address = payload.get("delivery_address", "")
            
            if not isinstance(payload["delivery_quantity"], int):
                return error_response("Invalid Delivery Quantity Format. It should be an integer.", 400)
            
            if not re.match(r'^\d{4}-\d{2}-\d{2}$', payload["delivery_date"]):
                return error_response("Invalid Delivery Date Format. It should be in YYYY-MM-DD format.", 400)
            
            if "delivery_address" in payload and not isinstance(delivery_address, str):
                return error_response("Invalid Address Format. It should be of type string.", 400)
            
            if not (isinstance(payload.get("customer_id"), str) and payload["customer_id"].strip() and len(payload["customer_id"]) == 24):
                return error_response("Invalid Customer ID Format. It should be a non-empty string.", 400)
                
        except Exception as e:
            return error_response(f"Internal Server Error => {str(e)}", 500)
        
        return f(payload, *args, **kwargs)
    return wrapper