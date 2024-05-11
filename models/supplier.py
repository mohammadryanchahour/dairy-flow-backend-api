from mongoengine import Document, StringField, DateTimeField, ObjectIdField

class Supplier(Document):
    name = StringField(required=True)
    address = StringField(required=True)
    phone = StringField(required=True)
    rate_id = ObjectIdField()
    created_at = DateTimeField(required=True)
    updated_at = DateTimeField(required=True)
