password = input("Enter password: ")

if len(password) >= 8 and any(char.isdigit() for char in password):
    print("Strong")
else:
    print("Weak")
