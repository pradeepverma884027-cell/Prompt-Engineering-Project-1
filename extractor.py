import json

sample_data = {
    "customer_name": "Pradeep Kumar",
    "order_number": "ORD789",
    "email": "pradeep@gmail.com",
    "phone": None
}

print(json.dumps(sample_data, indent=4))
