arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
result = []
while arr1 and arr2:
    if arr1[0] < arr2[0]:
        result.append(arr1.pop(0))
    else:
        result.append(arr2.pop(0))
if arr1:
    result.extend(arr1)
if arr2:
    result.extend(arr2)
print(*result)