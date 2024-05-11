from datetime import datetime
from bson import ObjectId
from helpers.custom_responses import error_response
from models.customer import Customer
from models.rates import Rates

def create_customer(validated_payload):
    try:
        name = validated_payload["name"]
        phone_number = validated_payload["phone"]
        address = validated_payload["address"]
        rate_id = validated_payload["rate_id"]
    
        rate = Rates.objects(id=ObjectId(rate_id)).first()

        if not rate:
            return None, error_response("Rate not found", 404)
        
        phone_already_exists = Customer.objects(phone=phone_number).first()
        
        if phone_already_exists:
            return None, error_response("Phone number already exists", 400)
        
        position = Customer.objects().count() + 1

        customer = Customer(
            name=name,
            phone=phone_number,
            address=address,
            rate_id=rate_id,
            position=position,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )

        customer.save()
        return customer, None

    
    except Exception as e:
        return error_response(f"Internal Server Error => {str(e)}", 500)
    
def get_all_customers():
    try:
        customers = Customer.objects().order_by("position")
        return customers, None
    
    except Exception as e:
        return None, error_response(f"Internal Server Error => {str(e)}", 500)
    
def get_customer_by_id(customer_id):
    try:
        # Ensure customer_id is a valid ObjectId before querying
        if not ObjectId.is_valid(customer_id):
            return None, error_response("Invalid customer ID", 400)
        
        customer = Customer.objects(id=ObjectId(customer_id)).first()

        if not customer:
            return None, error_response("Customer not found", 404)
        
        return customer, None
    
    except Exception as e:
        return error_response(f"Internal Server Error => {str(e)}", 500)    

def update_customer(customer_id, payload):
    try:
        # Retrieve the existing customer from the database
        existing_customer, error = get_customer_by_id(customer_id)
        if error:
            return None, error
        
        possible_fields = ['name', 'phone', 'address', 'rate_id', 'position']

        for field in possible_fields:
            if field in payload and not field == 'position':
                existing_customer[field] = payload[field]

            elif field in payload and field == 'position':
                existing_customer, error = update_customer_position(existing_customer["id"], payload[field])
                if error:
                    return None, error

        existing_customer["updated_at"] = datetime.now()
        existing_customer.save()
        
        return existing_customer, None

    except Exception as e:
        return None, error_response(f"Internal Server Error => {str(e)}", 500)

def update_customer_position(customer_id, new_position):
    try:
        # Retrieve the existing customer from the database
        existing_customer, error = get_customer_by_id(customer_id)
        if error:
            return None, error

        current_position = existing_customer["position"]

        if new_position == current_position:
            return existing_customer, None

        shift = 1 if new_position < current_position else -1

        # Retrieve the list of customers affected by the movement
        if new_position < current_position:
            affected_customers = Customer.objects(position__lt=current_position, position__gte=new_position)
        else:
            affected_customers = Customer.objects(position__gt=current_position, position__lte=new_position)

        for customer in affected_customers:
            customer["position"] += shift
            customer["updated_at"] = datetime.now()
            customer.save()

        existing_customer["position"] = new_position
        customer["updated_at"] = datetime.now()
        existing_customer.save()

        return existing_customer, None

    except Exception as e:
        return None, error_response(f"Internal Server Error => {str(e)}", 500)


def get_filtered_customers(filters):
    try:
        query = construct_query(filters)
        customers = Customer.objects(__raw__=query)
        return customers, None
    except Exception as e:
        return None, str(e)


def construct_query(filters):
    query = {}
    search_query = filters.get('query')
    filter_types = filters.get('type', [])
    
    if search_query:
        query['$or'] = [{filter_type: {'$regex': search_query, '$options': 'i'}} for filter_type in filter_types]
    
    return query

