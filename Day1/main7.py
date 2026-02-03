user_details = [
    {"username":"aditya","password":"abc@123","role":"admin"},
    {"username":"raMhul","password":"xyz@123","role":"user"},
    ]
    
username = input("Enter username: ")
password = input("Enter password: ")

user_found = False

for user in user_details:
    if user["username"] == username:
        user_found = True
        if user_found:
            if user["password"] == password:
                print("Login successful!")
                print("Role:", user["role"])
                break
            else:
                print("Incorrect password")
                break
if not user_found:
    print("User not found")