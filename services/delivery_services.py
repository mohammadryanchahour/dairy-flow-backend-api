from datetime import datetime
from bson import ObjectId
from helpers.custom_responses import error_response
from services.customer_services import get_customer_by_id
from models.delivery import Delivery
from services.transaction_services import create_transaction

def create_delivery(validated_payload):
    try:
        delivery_quantity = int(validated_payload["delivery_quantity"])
        delivery_date = validated_payload["delivery_date"]
        customer_id = validated_payload["customer_id"]
        delivery_address = validated_payload.get("delivery_address")
        
        customer, error = get_customer_by_id(customer_id)

        if error:
            return None, error
        
        if multiple_delivery_per_day(customer_id, delivery_date):
            return None, error_response("Duplicate delivery found for the customer on the same day", 400)
        
        delivery = Delivery(
            customer_id=ObjectId(customer_id),
            delivery_quantity=delivery_quantity,
            delivery_address=delivery_address,
            delivery_date=delivery_date,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )

        delivery.save()

        transaction, error = create_transaction(delivery, customer)

        if error:
            return None, error

        return delivery, None
    
    except Exception as e:
        return None, error_response(f"Internal Server Error => {str(e)}", 500)

def create_bulk_deliveries(payload_list):
    try:
        deliveries = []
        for payload in payload_list:
            delivery_quantity = int(payload["delivery_quantity"])
            delivery_date = payload["delivery_date"]
            customer_id = payload["customer_id"]
            delivery_address = payload.get("delivery_address")
            
            customer, error = get_customer_by_id(customer_id)

            if error:
                deliveries.append({"error": error})
                continue

            if multiple_delivery_per_day(customer_id, delivery_date):
                deliveries.append({"error": "Duplicate delivery found for the customer on the same day"})
                continue
            
            delivery = Delivery(
                customer_id=ObjectId(customer_id),
                delivery_quantity=delivery_quantity,
                delivery_address=delivery_address,
                delivery_date=delivery_date,
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
            deliveries.append(delivery)

        Delivery.objects.insert(deliveries)

        return deliveries, None

    except Exception as e:
        return None, error_response(f"Internal Server Error => {str(e)}", 500)
    
def get_all_deliveries():
    try:
        deliveries = Delivery.objects().order_by("delivery_date")
        return deliveries, None
    
    except Exception as e:
        return None, error_response(f"Internal Server Error => {str(e)}", 500)
    
def get_delivery_by_id(delivery_id):
    try:
        delivery = Delivery.objects(id=delivery_id).first()
        
        if delivery:
            return delivery, None
        else:
            return None, error_response("Delivery not found", 404)
    
    except Exception as e:
        return None, error_response(f"Internal Server Error => {str(e)}", 500)
    
def multiple_delivery_per_day(customer_id, delivery_date):
    existing_delivery = Delivery.objects(customer_id=ObjectId(customer_id), delivery_date=delivery_date).first()
    if existing_delivery:
        return True  
    return False
