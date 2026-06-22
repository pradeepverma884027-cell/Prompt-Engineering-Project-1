import streamlit as st
import json
import re

st.title("Prompt Engineering Data Extractor")

text = st.text_area("Enter Raw Text")

if st.button("Extract"):

    name = None
    order = None
    email = None
    phone = None

    name_match = re.search(r"Name:\s*(.*)", text)
    order_match = re.search(r"Order Number:\s*(.*)", text)
    email_match = re.search(r"Email:\s*(.*)", text)
    phone_match = re.search(r"Phone:\s*(.*)", text)

    if name_match:
        name = name_match.group(1)

    if order_match:
        order = order_match.group(1)

    if email_match:
        email = email_match.group(1)

    if phone_match:
        phone = phone_match.group(1)

    result = {
        "customer_name": name,
        "order_number": order,
        "email": email,
        "phone": phone
    }

    st.json(result)
