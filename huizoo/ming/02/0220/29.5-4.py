arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
result = []
i, j = 0, 0
while i < 4 and j < 4:
    if arr1[i]>arr2[j]:
        result.append(arr2[j])
        j += 1
    else:
        result.append(arr1[i])
        i += 1
result += arr1[i:] + arr2[j:]
print(*result)