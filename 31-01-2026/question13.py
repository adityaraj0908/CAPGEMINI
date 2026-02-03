n = int(input())
names = input().split()

result = ""

for name in names:
    result = result + name[0].upper()

print(result)
