N = int(input())
A = list(map(int, input().split()))


A = sorted(A)
max_val = A[-1]
second_max = A[-2]

avg = (max_val + second_max) / 2


for i in range(N):
    if A[i] < avg:
        A[i] = 0

print(sum(A))
