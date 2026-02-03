
income = float(input("Enter annual income: "))

if income<= 250000:
    print("No tax")
    
elif income>250000 and income<500000:
    print(f"Tax: {income-250000}*0.5")
    
elif income>500000 and income<1000000:
    print(f"Tax: {(250000*0.5) + (income-500000)*0.20}")
    
else:
    print(f"Tax: {(250000*0.5) + (500000*0.20) + (income-1000000)*0.30}")
