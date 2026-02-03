transaction = []
flags = 0
while True:
    if flags<2:
        amount = float(input("Enter the amount: "))
        if amount<100:
            pass
        if amount>100 and amount<=50000:
            transaction.append(amount)
        else:
            transaction.append(amount)
            flags+=1
    else:
        print("More than 2 flags. Processing stopped")
        break

print(f"Total number of transations: {len(transaction)}")
print("Flagged Transactions: ")
for t in transaction:
    if t>50000:
        print(t, end=" ")

