arr = []
for i in range(5):
    strings = input()
    arr.append(strings)

max_arr = 0
for i in range(5):
    if max_arr < len(arr[i]):
        max_arr = len(arr[i])
        arr1 = arr[i]

print(arr1)
