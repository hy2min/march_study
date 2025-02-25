arr1 = [list(map(int,input().split())) for _ in range(4)]
n = input()
arr2 = [list(map(int,input().split())) for _ in range(4)]

flag = 0
for i in range(4):
    for j in range(4):
        if arr1[i][j] == arr2[i][j] == 1:
            flag = 1
if flag == 1:
    print("걸리다")
else:
    print("걸리지않는다")
