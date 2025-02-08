N = int(input())
arr = [0] * 1001
s = 0
for _ in range(N):
    i, h = map(int, input().split())
    arr[i] = h

start = next(i for i in range(1001) if arr[i] > 0)
end = next(i for i in range(1000, -1, -1) if arr[i] > 0)
arr = arr[start:end+1]

reversed_arr = arr[::-1]
max_arr = max(arr)
if arr.count(max_arr) >= 2:
    max_index1 = arr.index(max_arr)
    max_index2 = len(arr) - reversed_arr.index(max_arr) - 1
    s += max_arr * (abs(max_index1 - max_index2) + 1)
else:
    max_index1 = arr.index(max_arr)
    max_index2 = arr.index(max_arr)
    s += max_arr

def Carculate_left(lst):
    global s
    if not lst:
        return []
    length = len(lst)
    height = max(lst)
    max_index = lst.index(height)
    s += height * (length - max_index)
    return lst[:max_index]

def Carculate_right(lst):
    global s
    if not lst:
        return []
    length = len(lst)
    height = max(lst)
    max_index = lst.index(height)
    s += height * (max_index + 1)
    return lst[max_index+1:]

arr2 = arr[:max_index1]
arr3 = arr[max_index2+1:]
while arr2 or arr3:
    if arr2:
        arr2 = Carculate_left(arr2)
    if arr3:
        arr3 = Carculate_right(arr3)

print(s)
