# import sys
# sys.stdin = open("input.txt","r")

arr = [list(input()) for _ in range(4)]
cnt_list = []
value_list = []

for i in range(3):
    tmp = 0
    for j in range(4):
        if arr[j][i] == '_':
            tmp += 1
    cnt_list.append(tmp)

for i in range(3):
    row = []
    for j in range(4):
        if arr[j][i] != '_':
            row.append(arr[j][i])
    value_list.append(row)

for i in range(3):
    n = cnt_list[i]
    for j in range(n):
        arr[j][i] = '_'
    for j in range(4-n):
        arr[n+j][i] = value_list[i][j]

for i in range(4):
    for j in range(3):
        print(arr[i][j],end='')
    print()