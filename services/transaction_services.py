from datetime import datetime
from bson import ObjectId
from helpers.custom_responses import error_response
from models.transaction import Transaction
from models.rates import Rates

def create_transaction(delivery, customer):
    try:
        rate_id = customer["rate_id"]
        rate = Rates.objects(id=ObjectId(rate_id)).first()
        delivery_quantity = delivery["delivery_quantity"]
        transaction_amount = delivery_quantity * rate["rate"]
        
        transaction = Transaction(
            delivery_id=delivery["id"],
            customer_id=customer["id"],
            transaction_amount=transaction_amount,
            transaction_date=delivery["delivery_date"],
            is_paid=False,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )

        transaction.save()

        return transaction, None

    except Exception as e:
        return None, error_response(f"Internal Server Error => {str(e)}", 500)