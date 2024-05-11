from mongoengine import Document, StringField, DateTimeField, ObjectIdField, ListField, IntField
from enum import Enum

class BillStatus(Enum):
    PENDING = "Pending"
    PAID = "Paid"
    OVERDUE = "Overdue"
    CANCELLED = "Cancelled"

class Bills(Document):
    customer_id = ObjectIdField()
    total_amount_due = IntField()
    status = StringField(default=BillStatus.PENDING.value)
    paid_at = DateTimeField()
    transactions = ListField()
    created_at = DateTimeField(required=True)
    updated_at = DateTimeField(required=True)
