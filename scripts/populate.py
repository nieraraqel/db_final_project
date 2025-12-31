import requests
import random
from datetime import date

BASE_URL = "http://127.0.0.1:8000"

# create chore types
chore_types = [
    {"name": "Electricity", "is_have_counter": True, "cost_per_month": 1200.00},
    {"name": "Water", "is_have_counter": True, "cost_per_month": 800.00},
    {"name": "Gas", "is_have_counter": True, "cost_per_month": 900.00},
    {"name": "Maintenance", "is_have_counter": False, "cost_per_month": 1500.00},
]

chore_ids = []
for chore in chore_types:
    r = requests.post(f"{BASE_URL}/chore-types/", json=chore)
    r.raise_for_status()
    chore_ids.append(r.json()["id"])

# create apartments
apartment_ids = []

for i in range(1, 51):
    apartment = {
	"owner": f"Owner {i}",
        "street": random.choice(["Main", "High", "Green", "Central"]),
        "n_of_house": random.randint(1, 20),
        "n_of_apartment": i
    }

    r = requests.post(f"{BASE_URL}/apartment/", json=apartment)
    r.raise_for_status()
    apartment_ids.append(r.json()["id"])

# create payments
for _ in range(200):
    payment = {
        "chore_id": random.choice(chore_ids),
        "apartment_id": random.choice(apartment_ids),
        "cost": round(random.uniform(500, 3000), 2),
        "month_year": random.choice(["01-2024", "02-2024", "03-2024"]),
        "date_of_deposit": str(date.today())
    }

    r = requests.post(f"{BASE_URL}/payments/", json=payment)
    r.raise_for_status()

print("Database successfully populated via REST API")
