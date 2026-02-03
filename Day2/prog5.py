quantity = int(input("Enter the quantity:"))

if quantity<1 or quantity>5:
    print("Invalid Order")
else:
    attempt = 0
    payment_status = False
    
    while attempt<3:
        status = input("Enter payment status (pass/fail)")
        if status == "pass":
            print("Payment completed. Order Placed")
            payment_status= True
            break
        else:
            attempt+=1
            if attempt<3:
                print("Payment failed. Retrying")
            else:
                print("Payment failed. Order cancelled.")