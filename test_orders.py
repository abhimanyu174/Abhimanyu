orders = [
    {"order_id": 1, "amount": 500},
    {"order_id": 2, "amount": 800},
    {"order_id": 3, "amount": 0}
]

order_ids = [order["order_id"] for order in orders]

# Test for duplicate order IDs
assert len(order_ids) == len(set(order_ids)), "Duplicate IDs found!"

# Test for null order IDs
assert all(order["order_id"] is not None for order in orders), "Null IDs found!"

print("All order tests passed!")