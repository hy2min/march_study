arr = list(map(int, input().split()))


pivot = arr[0]

left = 1
right = len(arr)-1

while left <= right:
    while left <= right and pivot >= arr[left]:
        left += 1
    while left <= right and pivot <= arr[right]:
        right -= 1

    if left < right:
        arr[left], arr[right] = arr[right], arr[left]

arr[0], arr[right] = arr[right], arr[0]

print(*arr)