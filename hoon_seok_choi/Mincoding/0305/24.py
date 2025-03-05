
def binary_search(arr) :
    # arr.sort()
    start = 0
    end = len(arr) -1

    while start <= end :
        mid = (start + end) // 2

        if arr[mid] == '#' :
            start = mid + 1
        else : 
            end = mid -1

    return start

arr = list(input())

a = binary_search(arr) * 10
print(f'{a}%')
