print("ELECTRICITY BILL CALCULATOR")

elec_unit = float(input("Enter number of units consumed: "))
if elec_unit<=100:
    print(f"Bill: {elec_unit*5}")
elif elec_unit >100 and elec_unit<=200:
    print(f"Bill: {100*5+ (elec_unit-100)*7}")
else:
     print(f"Bill: {100*5+ 100*7 + (elec_unit-200)*10}")
