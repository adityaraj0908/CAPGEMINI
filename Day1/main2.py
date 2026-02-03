products = []
total_cost = 0
quantity = 0

while True:
    name = input("Enter product name (or STOP to finish): ")
    if name == "STOP":
        break
    price = float(input("Enter the price of the product: "))
     
    products.append((name,price))
    total_cost+= price
    quantity+=1
print(products)
print(f"Number of products: {quantity}")
print(f"Total cost: {total_cost}")
    