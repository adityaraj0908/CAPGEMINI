my_queue = []
max_capacity = 5

while True:
    person = input("Enter the person (-99 for VIP): ")

    if person == "-99":
        print("VIP entered. System stopped")
        break 
    else:
        if len(my_queue)<max_capacity:
            my_queue.append(person)
        else:
            print("Maximum capacity reached.")
            break
print("Sequence: ", end="")
print(my_queue)

