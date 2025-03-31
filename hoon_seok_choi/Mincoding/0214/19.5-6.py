arr = [
    [3, 5, 1],
    [3, 8, 1],
    [1, 1, 5]
]

arr2 = [list(map(int,input().split())) for _ in range(2)]
max_v =  -21e8
max_p = [0,0]

def f_sum(y,x) :
    Sum = 0

    for i in range(2) :
        for j in range(2) :
            if arr2[i][j] == 1 :
                Sum += arr[i+y][j+x]
    return Sum

for i in range(2) :
    for j in range(2) :
        ret = f_sum(i,j)
        if ret > max_v :
            max_v = ret
            max_p[0] = i
            max_p[1] = j


print(f"({max_p[0]},{max_p[1]})")
