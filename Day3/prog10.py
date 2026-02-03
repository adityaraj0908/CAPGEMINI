a = input("Enter your string: ")

if a.lower() == a[::-1].lower():
    print("Palindrome")
else:
    print("Not Palindrome")
