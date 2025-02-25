arr = list(map(str, input().split()))
arr2 = list(map(str, input().split()))
arr3 =[]

for i in range(len(arr)) :
    total = int(arr[i]) + int(arr2[len(arr)-1 - i])
    arr3.append(total)

print(*arr3,sep=" ")