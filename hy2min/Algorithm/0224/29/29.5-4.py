arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

ret = []


i = 0
j = 0
while i <4 and j <4:
    if arr1[i] > arr2[j]:
        ret.append(arr2[j])
        j += 1
    else:
        ret.append(arr1[i])
        i += 1

if i < 4:
    ret.extend(arr1[i:])
if j < 4:
    ret.extend(arr2[j:])    

print(*ret)