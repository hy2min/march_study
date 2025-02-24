arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
result = []
i, j = 0, 0
while len(result) < 8:
    if arr1[i] > arr2[j]:
        result.append(arr2[j])
        j += 1
    else : 
        result.append(arr1[i])
        i += 1
    if i > 3 or j > 3 :
        result += arr1[i:] + arr2[j:]
        break

print(*result)