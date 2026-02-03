# with open("data.txt", "w") as f:
#     f.write("Python File Handling")

# with open("data.txt", "r") as f:
#     print(f.read())




# age = int(input("Enter customer's age?: "))
# timing = float(input("Enter show timing: "))
# price = 0

# if timing == 11.30:
#     price = 1
# else:
#     price = 2

# print(f"$ {price}.00")








# def leap_year(year):
#     return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

# year = int(input("Enter year: "))

# if leap_year(year):
#     print(f"{year} is leap year")
# else:
#     next_year = year+1
#     while not leap_year(next_year):
#         next_year+=1
#     print(f"{next_year} is the nearest leap year")

    





# def get_number():
#     n = input()
#     k = int(input())

#     if k>len(n):
#         return -1
#     else:
#         return int(n[k-1])
    
# print(get_number())








# n = int(input("Enter no of overs: "))

# initial = 95.0
# diff = 20.5

# for i in range(n):
#     print(initial+diff*i, end=" ")








# n = int(input())

# while n>0:
#     print(n*"* ")
#     n-=1






## 6
# n = int(input())

# start = (n*(n+1))//2

# for row in range(n,0,-1):
#     for i in range(row):
#         print(f"* {start}", end=" ")
#         start-=1
#     print()









# n = int(input())
# my_list=[]

# for i in range(n):
#     my_list.append(int(input()))

# print(my_list)
# my_list.sort()
# print(my_list)

# val = 1

# for i in range(len(my_list)-1):
#     if(my_list[i+1]!=my_list[i]+1):
#         val=0
#         break
            
# print(val)




# n = int(input())
# start = 4

# for i in range(0,n+1):
#     start+=i*i
#     print(start, end=" ")






# def count_digits(n):
#     if n == 0:
#         return 0
#     return 1 + count_digits(n // 10)

# n = int(input())

# if n==0:
#     print(1)
# else:
#     print(count_digits(n))








# def my_func(n):
#     if n == 0:
#         return 1
#     return 2 * my_func(n - 1)

# n = int(input())

# print(my_func(n))











# def fib(n):
#     if n == 1:
#         return 0
#     if n == 2 :
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)

# n = int(input())


# for i in range(1, n + 1):
#     print(fib(i), end=" ")

# print()
# print(fib(n))


# total 12










# def count_func(s):

#     if len(s) == 0:
#         return 0

#     if s[0].isalnum():
#         return 1 + count_func(s[1:])
#     else:
#         return count_func(s[1:])


# s = input()

# if len(s) == 0:
#     print(-1)
# else:
#     print(count_func(s))











# s = input()
# result = []
# word = ""

# for i in range(len(s) - 1, -1, -1):
#     if s[i] != " ":
#         word = s[i] + word
#     else:
#         result.append(word)
#         word = ""

# result.append(word)
# print(" ".join(result))













# n = int(input())

# matrix = []
# for _ in range(n):
#     row = list(map(int, input().split()))
#     matrix.append(row)

# is_upper = True

# for i in range(n):
#     for j in range(n):
#         if i > j and matrix[i][j] != 0:
#             is_upper = False
#             break
#     if not is_upper:
#         break

# if is_upper:
#     print("Upper triangular matrix")
# else:
#     print("Not an Upper triangular matrix")
















# n = int(input())

# matrix = []
# for i in range(n):
#     row = list(map(int, input().split()))
#     matrix.append(row)

# for j in range(n):
#     col_max = matrix[0][j]
#     for i in range(1, n):
#         if matrix[i][j] > col_max:
#             col_max = matrix[i][j]
#     print(col_max, end=" ")











# n = int(input())

# matrix = []
# for i in range(n):
#     row = list(map(int, input().split()))
#     matrix.append(row)

# for i in range(n):

#     row = matrix[i][::-1]
    
#     for j in range(n):
#         row[j] = 1-row[j]
#     print(row)




# n = int(input())
# count = 0
# my_list = list(map(int,input().split()))

# for i in range(n):
#     if my_list[i]%3 == 0:
#         count+=1

# print(count)











# H, V, Vn = map(int, input().split())

# ratio = V / Vn
# height = H * (ratio ** 2)

# print(int(height))


















# s1 = input().strip()
# s2 = input().strip()

# max_len = 0
# best_sub = ""

# n = len(s1)


# for i in range(n):
#     for j in range(i + 1, n + 1):
#         sub = s1[i:j]
        
#         if sub in s2:
#             length = j - i
            
#             if length > max_len:
#                 max_len = length
#                 best_sub = sub

# print(best_sub)
# if max_len == 0:
#     print(0)
# else:
#     ascii_sum = 0
#     for ch in best_sub:
#         ascii_sum += ord(ch)
    
#     print(ascii_sum)




















