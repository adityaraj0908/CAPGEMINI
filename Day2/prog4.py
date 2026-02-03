valid_numbers = []

while len(valid_numbers)<5:
    user_input = input("Enter your number(or exit): ")
    
    if user_input == "exit":
        print("Exited")
        break
    
    try:
        number = int(user_input)
        valid_numbers.append(number)
    except:
        print("Only numbers are valid")
        
print("Valid numbers entered are: ", valid_numbers)
        