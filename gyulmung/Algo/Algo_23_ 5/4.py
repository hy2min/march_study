arr = [[3, 5, 4, 1], [1, 1, 2, 3], [6, 7, 1, 2]]
lst = list(map(int, input().split()))
lst.append(lst[0])

def find_num(y, x):
    global arr, lst

    for i in range(4):
        if arr[y][x] == lst[i]:
            arr[y][x] = lst[i+1]
            return arr

for i in range(3):
    for j in range(4):
        find_num(i, j)

for i in arr:
    print( *i)