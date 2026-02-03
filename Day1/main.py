total_sales = 0
highest_order = {}
amount =0
orders = [
    {"order_id": 101, "customer": "Aditya", "amount": 1200},
    {"order_id": 102, "customer": "Harsh", "amount": 800},
    {"order_id": 103, "customer": "Rahul", "amount": 1500}
]

for order in orders:
    total_sales += order["amount"]
    if order["amount"] > amount:
        amount= order["amount"]
        highest_order = order
        

print(f"Total order value is: {total_sales}")
print(f"Customer with maximum order value is: {highest_order["customer"]}")
print(f"Orders with amount greater than 1000 are: \n")

for order in orders:
    if(order["amount"]>1000):
        print(order)

