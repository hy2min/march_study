arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
result = []

while True:
    if len(arr1) == 0 and len(arr2) == 0:
        break
    if len(arr1) == 0:
        result.append(arr2.pop(0))
    elif len(arr2) == 0:
        result.append(arr1.pop(0))
    else:
        if arr1[0] > arr2[0]:
            result.append(arr2.pop(0))
        else:
            result.append(arr1.pop(0))


print(*result)