a = float(input("Enter side a "))
b = float(input("Enter side b "))
c = float(input("Enter side c "))

if a!=0 and b!=0 and c!=0:
    if(a==b==c):
        print("Equilateral triangle")
    elif a==b or b==c or c==a:
        print("Isoceles triangle")
    elif a!=b!=c:
        print("Scalene Triangle")
    
else:
    print("Not a Triangle")
    