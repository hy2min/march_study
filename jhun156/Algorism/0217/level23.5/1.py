arr = [3,5,1,9,7]
lst = []
for i in range(4):
    lst.append(input())

a = lst.count("R")
b = 4 - a

if a == b:
    print(*arr)
elif a > b:
    for i in range(a-b):
        tmp = arr[4]
        for j in range(4,-1,-1):
            arr[j] = arr[j-1]
        arr[0] = tmp
    print(*arr)
else:
    for i in range(b-a):
        tmp = arr[0]
        for j in range(1,5):
            arr[i-1] = arr[i]
        arr[4] = tmp
    print(*arr)