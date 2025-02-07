arr = list(input())

def maxIndex(arr):
    count = 0
    point = 0
    for i in range(len(arr)):
        if ord(arr[i]) > count:
            count = ord(arr[i])
            point = i
    return point

def minIndex(arr):
    count = 1e8
    point = 0
    for i in range(len(arr)):
        if ord(arr[i]) < count:
            count = ord(arr[i])
            point = i
    return point

print(f'{maxIndex(arr)}\n{minIndex(arr)}')