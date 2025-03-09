import copy
arr = [
    ['A','B','C','E','F','G'],
    ['H','I','J','K','L','M'],
    ['N','O','P','Q','R','S'],
]
arr2 = copy.deepcopy(arr)
d = [(-1, 0), (1, 0), (0, 0), (0, 1), (0, -1)]
st = list(input())
def turn(y, x):
    for dy, dx in d:
        ny, nx = y+dy, x+dx
        if ny<0 or nx<0 or ny>=3 or nx>=6: continue
        if arr[ny][nx] == '#':
            arr[ny][nx] = arr2[ny][nx]
        else:
            arr[ny][nx] = '#'
for alp in st:
    for i in range(3):
        for j in range(6):
            if arr2[i][j] == alp:
                turn(i, j)
print('\n'.join(''.join(row) for row in arr))