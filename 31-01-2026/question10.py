N = int(input())
P = int(input())

total_time = 240
remaining_time = total_time - P

time_used = 0
count = 0

for i in range(1, N + 1):
    time_used = time_used + (5 * i)

    if time_used <= remaining_time:
        count = count + 1
    else:
        break

print(count)
