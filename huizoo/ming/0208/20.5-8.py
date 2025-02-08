arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
result = []
i, j = 0, 0
while j < 4 and i < 4 :
        if arr1[i] < arr2[j] : 
            result.append(arr1[i])
            i += 1
        else : 
            result.append(arr2[j])
            j += 1
result.extend(arr1[i:])
result.extend(arr2[j:])

print(*result)