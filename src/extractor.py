# extractor.py

import re
import json
from sample_data import sample_data


def extract_data(text):
    result = {
        "customer_name": None,
        "order_number": None,
        "email": None,
        "phone": None
    }

    name_match = re.search(r"Name:\s*(.*)", text, re.IGNORECASE)
    order_match = re.search(r"Order Number:\s*(.*)", text, re.IGNORECASE)
    email_match = re.search(r"Email:\s*([\w\.-]+@[\w\.-]+)", text, re.IGNORECASE)
    phone_match = re.search(r"Phone:\s*(\d+)", text, re.IGNORECASE)

    if name_match:
        result["customer_name"] = name_match.group(1).strip()

    if order_match:
        result["order_number"] = order_match.group(1).strip()

    if email_match:
        result["email"] = email_match.group(1).strip()

    if phone_match:
        result["phone"] = phone_match.group(1).strip()

    return result


print("=" * 50)
print("PROMPT ENGINEERING DATA EXTRACTION PROJECT")
print("=" * 50)

for i, text in enumerate(sample_data, start=1):
    print(f"\nSample {i}")
    print("-" * 30)

    extracted = extract_data(text)

    print(json.dumps(extracted, indent=4))
