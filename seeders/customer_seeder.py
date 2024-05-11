import os
import random
import sys
import uuid

from bson import ObjectId
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from datetime import datetime
from dotenv import load_dotenv
from mongoengine import connect
from models.customer import Customer

load_dotenv()

# Connect to MongoDB
mongo_uri = os.getenv("MONGO_DB_URI")
if not mongo_uri:
    raise ValueError("MONGO_DB_URI environment variable is not set")

connect(host=mongo_uri)

def generate_address():
    # Generate a random address using UUID
    return str(uuid.uuid4())

def generate_name():
    # Generate a random name consisting of alphabets
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    name_length = random.randint(5, 10)  # You can adjust the name length range as needed
    name = ''.join(random.choice(alphabet) for _ in range(name_length))
    return name

def generate_phone_number():
    # Generate a random phone number matching the pattern '^03\d{2}-\d{7}$'
    return f"03{random.randint(10, 99)}-{random.randint(1000000, 9999999)}"


def generate_customers(num_customers=50):
    customers = []
    for _ in range(num_customers):
        customer = Customer(
            name=generate_name(),
            address=generate_address(),
            phone=generate_phone_number(),
            position=random.randint(1, 100),
            rate_id=ObjectId("662ca968889346c220e405c1"),
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        customers.append(customer)
    return customers

def seed_customers(customers):
    for customer in customers:
        customer.save()

if __name__ == "__main__":
    # Generate 50 customers
    customers_to_seed = generate_customers()

    # Seed the customers into the database
    seed_customers(customers_to_seed)
