arr = [
    [3, 1, 9],
    [7, 2, 1],
    [1, 0, 8]
]


arr2 = [list(map(int,input().split())) for _ in range(3)]

for i in range(3) :
    for j in range(3) :
        if arr2[i][j] == 1 and 3>= arr[i][j] <=5 :
            print('발견')
            break
        else : 
            print('미발견')
            break