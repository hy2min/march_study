arr = [[0]*4 for _ in range(4)]

for i in range(3) : 
    arr[i][0], arr[i][1], arr[i][2] = map(int, input().split())

for i in range(3) : 
    Sum = 0
    for j in range(3) : 
        Sum += arr[i][j]
    arr[i][3] = Sum

for j in range(3) : 
    Sum = 0
    for i in range(3) : 
        Sum += arr[i][j]
    arr[3][j] = Sum

Sum = 0
for i in range(3) : 
    Sum += arr[i][i]
arr[3][3] = Sum


print('\n'.join(' '.join(map(str, row)) for row in arr))