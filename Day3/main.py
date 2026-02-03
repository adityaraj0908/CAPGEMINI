# # prog1
# a = int(input("enter first number"))
# b = int(input("enter second number"))

# print(f"Before Swap a: {a} and b: {b}")
# a,b = b,a
# print(f"Before Swap a: {a} and b: {b}")




# # prog2
# a = input("Enter your input: ")
# print(a)



# # prog3
# a = int(input("Enter your number: "))

# if a%2==0:
#     print("Even")
# else:
#     print("Odd")


# # prog4
# a = int(input("Enter the number: "))

# for i in range(0,11):
#     print(f"{a} x {i} = {a*i}")


# # prog5
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a >= b and a >= c:
#     print("Largest:", a)
# elif b >= a and b >= c:
#     print("Largest:", b)
# else:
#     print("Largest:", c)


# # prog6
# c = float(input("Enter temperature in Celsius: "))
# f = (c * 9/5) + 32
# print("Fahrenheit:", f)



# prog7
# n = int(input("Enter number: "))

# fact = 1
# for i in range(1, n + 1):
#     fact *= i

# print("Factorial:", fact)


# # prog8
# s = input("Enter string: ").lower()

# count = 0
# for ch in s:
#     if ch in "aeiou":
#         count += 1

# print("Vowels count:", count)


# # prog9
# a = input("Enter the string: ")
# print(a[::-1])


# # prog10
# n = int(input("Enter number: "))
# temp = n
# rev = 0

# while n > 0:
#     rev = rev * 10 + n % 10
#     n //= 10

# if temp == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# # prog11
# n = int(input("Enter n: "))
# sum = 0

# for i in range(1, n + 1):
#     sum += i

# print("Sum:", sum)



# # prog12
# import random

# number = random.randint(1, 10)

# guess = int(input("Guess number (1-10): "))

# if guess == number:
#     print("Correct!")
# else:
#     print("Wrong! Number was", number)


# # prog13
# for i in range(1, 101):
#     print(i)



# prog14
# year = int(input("Enter year: "))

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print("Leap Year")
# else:
#     print("Not Leap Year")



# # prog15
# n = int(input("Enter n: "))

# a, b = 0, 1

# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b



# # prog16
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# while b != 0:
#     a, b = b, a % b

# print("GCD:", a)








# # prog17
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# x, y = a, b

# while y != 0:
#     x, y = y, x % y

# gcd = x
# lcm = (a * b) // gcd

# print("LCM:", lcm)







# # prog18
# ch = input("Enter a character: ").lower()

# if ch in "aeiou":
#     print("Vowel")
# else:
#     print("Consonant")





# # prog19
# n = int(input("Enter number: "))
# sum = 0

# while n > 0:
#     sum += n % 10
#     n //= 10

# print("Sum of digits:", sum)



# # prog20
# lst = [10, 20, 4, 45, 99]

# largest = second = -1

# for i in lst:
#     if i > largest:
#         second = largest
#         largest = i
#     elif i > second and i != largest:
#         second = i

# print("Second largest:", second)



# prog21
# n = int(input("Enter number: "))
# count = 0

# while n > 0:
#     count += 1
#     n //= 10

# print("Digits:", count)



# prog22
for num in range(1, 101):
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        d = temp % 10
        total += d ** digits
        temp //= 10

    if total == num:
        print(num)






# # prog23
# n = int(input("Enter rows: "))

# for i in range(1, n + 1):
#     print("* " * i)


# # prog24
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# op = input("Enter operator (+ - * /): ")

# if op == '+':
#     print(a + b)
# elif op == '-':
#     print(a - b)
# elif op == '*':
#     print(a * b)
# elif op == '/':
#     print(a / b)
# else:
#     print("Invalid operator")




# # prog25
# ch = input("Enter character: ")
# print("ASCII value:", ord(ch))



# # prog26
# n = int(input("Enter decimal number: "))
# binary = ""

# while n > 0:
#     binary = str(n % 2) + binary
#     n //= 2

# print("Binary:", binary)




# # prog27
# n = int(input("Enter number: "))
# print("Square root:", n ** 0.5)



# # prog28
# lst = [1, 2, 3, 4, 5, 6]
# sum = 0

# for i in lst:
#     if i % 2 == 0:
#         sum += i

# print("Sum of even numbers:", sum)




# # prog29
# n = int(input("Enter number: "))

# if n <= 1:
#     print("Not Prime")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")



# # prog30
# n = int(input("Enter number: "))

# for i in range(1, n + 1):
#     print("Cube of", i, "=", i ** 3)



