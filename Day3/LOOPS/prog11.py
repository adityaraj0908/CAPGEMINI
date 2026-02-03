s = input("Enter string: ")

letters = digits = special = 0

for ch in s:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1

print("Letters:", letters)
print("Digits:", digits)
print("Special symbols:", special)
