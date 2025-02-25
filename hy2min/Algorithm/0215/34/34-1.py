arr = [4, 4, 5, 7, 8, 10, 20, 22, 23, 24]
target = int(input())

def binary_search(arr, target):
    start, end = 0, len(arr)-1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            start = mid + 1        
        else:
            end = mid - 1
    return 0

if binary_search(arr,target):
    print("O")
else:
    print("X")