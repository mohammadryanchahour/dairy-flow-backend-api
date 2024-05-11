from mongoengine import Document, StringField, DateTimeField, ObjectIdField, IntField

class Customer(Document):
    name = StringField()
    address = StringField()
    phone = StringField()
    position = IntField()
    rate_id = ObjectIdField()
    created_at = DateTimeField(required=True)
    updated_at = DateTimeField(required=True)
