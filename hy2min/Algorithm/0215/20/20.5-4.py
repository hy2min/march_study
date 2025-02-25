a = [list(map(int, input().split())) for i in range(4)]
input()
b = [list(map(int, input().split())) for i in range(4)]
flag = 0
for i in range(4):
    for j in range(4):
        if a[i][j] == b[i][j] == 1:
            flag = 1
            break
    if flag:
        break

if flag:
    print('걸리다')
else:
    print('걸리지않는다')