def majority_element(arr):
    freq = {}

    for num in arr:
        if num in freq:
            freq[num] = freq[num] + 1
        else:
            freq[num] = 1

    n = len(arr)

    for key in freq:
        if freq[key] > n // 2:
            return key

    return -1


N = int(input())
arr = list(map(int,input().split()))
print(majority_element(arr))
