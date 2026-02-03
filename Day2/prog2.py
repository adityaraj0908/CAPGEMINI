upper_case = False
lower_case = False
contains_digits = False
contains_special_charcter = False

while True:
    password = input("Enter your password ")
    if len(password)<8:
        print("weak Password. Try Again")
    else:
        for ch in password:
            if ch.isupper():
                upper_case = True
            elif ch.islower():
                lower_case = True
            elif ch.isdigit():
                contains_digits = True
            else:
                contains_special_charcter = True
    
    
        if upper_case and lower_case and contains_special_charcter and contains_digits:
            print("Strong password")
            break
        else:
            print("Weak password. Try Again")
        
