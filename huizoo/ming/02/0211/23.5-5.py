arr = list(map(int, input().split()))
pivot = arr[0]
sorted_arr = sorted(arr[1:])
while arr[1:] != sorted_arr:
    a = 1
    b = 7
    while arr[a] <= pivot:
        a += 1
    while arr[b] >= pivot:
        b -= 1
    if b < a:
        break
    else:
        arr[a], arr[b] = arr[b], arr[a]
arr[0], arr[b] = arr[b], arr[0]

print(*arr)

