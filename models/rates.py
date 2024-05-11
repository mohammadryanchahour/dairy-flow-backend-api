from mongoengine import Document, IntField, DateTimeField, ListField

class Rates(Document):
    rate = IntField()
    customer_ids = ListField()
    supplier_ids = ListField()
    created_at = DateTimeField()
    updated_at = DateTimeField()
