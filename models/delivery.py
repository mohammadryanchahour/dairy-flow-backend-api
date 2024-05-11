from mongoengine import Document, StringField, DateTimeField, ObjectIdField, IntField, DateField

class Delivery(Document):
    customer_id = ObjectIdField()
    delivery_quantity = IntField()
    delivery_address = StringField()
    delivery_date = DateField()
    created_at = DateTimeField(required=True)
    updated_at = DateTimeField(required=True)
