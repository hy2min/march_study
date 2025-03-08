arr1 = [list(map(int, input().split())) for _ in range(4)]
a = input()
arr2 = [list(map(int, input().split())) for _ in range(4)]
flag = 0
for i in range(4):
    for j in range(4):
        if arr1[i][j] and arr2[i][j]:
            flag = 1
            if flag:
                break
    if flag:
        break
if flag:
    print('걸리다')
else:
    print('걸리지않는다')