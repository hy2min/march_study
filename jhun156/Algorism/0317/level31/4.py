arr = [list(input()) for _ in range(5)]
for i in range(5):
    arr[i][1],arr[i][3] = arr[i][3],arr[i][1]

flag = 0
for i in range(5):
    tmp = ''
    for j in range(5):
        tmp += arr[i][j]
    if tmp == 'MAPOM':
        flag = 1
        break
    if flag:
        break

if flag:
    print("yes")
else:
    print("no")