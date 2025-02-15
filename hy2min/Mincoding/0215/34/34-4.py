def binary_search(arr, n):
    start, end = 0, n*n-1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == '#':
            start = mid + 1
        else:
            end = mid - 1
    return start


n = int(input())
arr = []
for _ in range(n):
    arr.extend(input())

result = binary_search(arr, n)
print(result // n, result % n -1)
