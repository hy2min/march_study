arr = list(map(int, input().split()))
pivot = arr[0]
a = 1
b = 7
while a < b:
    while arr[a] < pivot:
        a += 1
        if a > 7: break
    while arr[b] > pivot:
        b -= 1
        if b < 1: break
    if a < b :
        arr[a], arr[b] = arr[b], arr[a]
        a = 1
        b = 7
arr[0], arr[b] = arr[b], arr[0]
print(*arr)