sum_of_even = 0
sum_of_odd = 0
range_of_numbers = int(input("Enter range: "))

for i in range(1,range_of_numbers):
    if i%2==0:
        sum_of_even+=i
    else:
        sum_of_odd+=i
print(sum_of_even)
print(sum_of_odd)