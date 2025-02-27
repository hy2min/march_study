arr = list(input())
for i in range(len(arr)-2):
    for j in range(i+1, len(arr)-1):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(arr)

# def maxIndex(arr):
