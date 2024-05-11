from mongoengine import Document, DateTimeField, ObjectIdField, IntField, DateField, BooleanField

class Transaction(Document):
    delivery_id = ObjectIdField()
    customer_id = ObjectIdField()
    transaction_amount = IntField()
    transaction_date = DateField()
    is_paid = BooleanField(default=False)
    created_at = DateTimeField(required=True)
    updated_at = DateTimeField(required=True)
