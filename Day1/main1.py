default_password = "adityaraj"

for attempt in range(3):
    password = input("Enter the password: ")
    if password == default_password:
        print("Login Successful")
        break
    else:
        print("Wrong password")
        if attempt == 2:
            print("Account locked")
