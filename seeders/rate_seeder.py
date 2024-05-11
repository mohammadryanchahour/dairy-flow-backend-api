import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from datetime import datetime
from dotenv import load_dotenv
from mongoengine import connect
from models.rates import Rates

load_dotenv()

# Connect to MongoDB
mongo_uri = os.getenv("MONGO_DB_URI")
if not mongo_uri:
    raise ValueError("MONGO_DB_URI environment variable is not set")

connect(host=mongo_uri)

# Define a function to seed data into the Rates model
def seed_rates():
    # Sample data
    rates_data = [
        {'rate': 100, 'customer_ids': [], 'supplier_ids': [], 'created_at': datetime.now(), 'updated_at': datetime.now()},
        {'rate': 150, 'customer_ids': [], 'supplier_ids': [], 'created_at': datetime.now(), 'updated_at': datetime.now()},
        {'rate': 200, 'customer_ids': [], 'supplier_ids': [], 'created_at': datetime.now(), 'updated_at': datetime.now()}
    ]

    # Seed data into the Rates model
    for rate_data in rates_data:
        rate = Rates(**rate_data)
        rate.save()

    print('Data seeded successfully!')

# Call the function to seed data
seed_rates()
