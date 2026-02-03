def lift_capacity(weights, capacity):
    total = sum(weights)
    if total <= capacity:
        return "Safe to move"
    else:
        return "Overloaded"

capacity = 500
weights = [70, 65, 80, 75, 90]

print(lift_capacity(weights, capacity))
