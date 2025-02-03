arr = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
]
a = int(input())
start = 2

for i in range(3):
    for j in range(start,3):
        arr[i][j] = a
        a += 1
    start -= 1

for i in arr:
    for j in i:
        print(j,end='')
    print()