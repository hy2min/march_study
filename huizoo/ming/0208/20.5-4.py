A = [list(map(int, input().split())) for _ in range(4)]
blank = input()
B = [list(map(int, input().split())) for _ in range(4)]
flag = 0
for i in range(4) : 
    for j in range(4) : 
        if A[i][j]+B[i][j] == 2 : 
            flag = 1
            break
    if flag : 
        break
if flag : 
    print('걸리다')
else : 
    print('걸리지않는다')