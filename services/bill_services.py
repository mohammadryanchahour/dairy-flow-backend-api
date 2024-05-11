from datetime import datetime
from enum import Enum
from bson import ObjectId
from helpers.custom_responses import error_response
from models.bills import Bills
from models.transaction import Transaction
from services.customer_services import get_all_customers

class BillStatus(Enum):
    PENDING = "Pending"
    PAID = "Paid"
    OVERDUE = "Overdue"
    CANCELLED = "Cancelled"
    
def generate_bills():
    try:
        generated_bills = []
        customers, error = get_all_customers()

        if error:
            return None, error

        for customer in customers:
            unpaid_transactions = Transaction.objects(customer_id=ObjectId(customer["id"]), is_paid=False)

            if unpaid_transactions:
                total_amount_due = sum(transaction.transaction_amount for transaction in unpaid_transactions)

                unpaid_transaction_ids = [str(transaction.id) for transaction in unpaid_transactions]

                bill = Bills(
                    customer_id=customer.id,
                    total_amount_due=total_amount_due,
                    status=BillStatus.PENDING.value,
                    paid_at=None,
                    transactions=unpaid_transaction_ids,
                    created_at=datetime.now(),
                    updated_at=datetime.now()
                )

                bill.save()
                generated_bills.append(bill)

        return generated_bills, None

    except Exception as e:
        return None, error_response(f"Internal Server Error => {str(e)}", 500)
