a = input("Enter your data: ")

try:
    a = int(a)
    print(a*a)
except:
    print(a[::-1])