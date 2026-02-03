
count = 0

N = int(input())

my_list = list(map(int,input().split()))

for i in range(N):
    if my_list[i] == 0:
        count+=1

print(count)





