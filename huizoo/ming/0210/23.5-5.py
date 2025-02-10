arr = list(map(int, input().split()))
pivot = arr[0]
a = 1
b = 7
while a <= b : 
    if arr[a] > pivot and arr[b] < pivot : 
        arr[a], arr[b] = arr[b], arr[a]
    a += 1
    b -= 1
    if a == b : 
        b -= 1
arr[0], arr[b] = arr[b], arr[0]

print(*arr)

