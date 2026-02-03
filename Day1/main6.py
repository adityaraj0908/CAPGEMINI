balance = 5000

withdrawal = int(input("Enter the withdrawal amount: "))
if(withdrawal>balance):
    print("Insufficient balance")
else:
    if(withdrawal%100 == 0):
        balance-=withdrawal
        print(f"Remaining balance: {balance}")
    else:
        print("withdrawal amount should be multiple of 100")