arr = [3, 7, 4, 1, 2, 6]


univer = [list(map(int,input().split())) for _ in range(2)]

for i in range(2) : 
    for j in range(2) :
        if univer[i][j] in arr :
            print('OK', end=" ")
        else :
            print('NO')
    print()