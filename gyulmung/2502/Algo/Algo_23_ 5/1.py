arr = [3, 5, 1, 9, 7]

def Right():
    global arr
    a = 0
    a = arr[-1]
    for i in range(3, -1, -1):
        arr[i+1] = arr[i]
    arr[0] = a
    return arr

def Left():
    global arr
    a = 0
    a = arr[0]
    for i in range(1, 5, 1):
        arr[i-1] = arr[i]
    arr[-1] = a
    return arr

for i in range(4):
    change = input()
    if change == 'R':
        Right()
    elif change == 'L':
        Left()
print(*arr)