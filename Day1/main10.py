arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]

common = []

for i in arr1:
    for j in arr2:
        if i == j and i not in common:
            common.append(i)

print(common)
