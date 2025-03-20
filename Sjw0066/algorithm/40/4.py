arr=[list(map(int,input().split())) for _ in range(7)]

result=[[-21e8]*3 for _ in range(7)]
result[0][0]=arr[0][0]


for i in range(1,7):
    for j in range(3):
        if arr[i][j] == 0 : continue
        j1=j-1
        j2=j
        j3=j+1
        if j1<0:
            result[i][j] = max(result[i-1][j2],result[i-1][j3])+arr[i][j]
        elif j3>2:
            result[i][j] = max(result[i-1][j2],result[i-1][j1])+arr[i][j]
        else:
            result[i][j] = max(result[i-1][j1],result[i-1][j2],result[i-1][j3])+arr[i][j]

print(max(result[6]))

