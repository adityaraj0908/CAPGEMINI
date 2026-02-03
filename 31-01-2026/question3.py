def completed_kms(N):
    total = 0

    for i in range(1, N + 1):
        if i % 2 == 0:
            total = total + i

    return total


N = int(input())
print(completed_kms(N))