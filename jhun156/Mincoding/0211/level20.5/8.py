arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
result = []
i = 0

while i < 8:
    if len(arr1) == 0:
        Min = min(arr2)
        result.append(Min)
        arr2.remove(Min)
        i += 1
    elif len(arr2) == 0:
        Min = min(arr1)
        result.append(Min)
        arr1.remove(Min)
        i += 1
    else:
        lst = []
        lst.extend([min(arr1),min(arr2)])
        Min = min(lst)
        result.append(Min)
        if Min in arr1:
            arr1.remove(Min)
        else:
            arr2.remove(Min)
        i += 1

print(*result)