arr=[[0]*3 for _ in range(6)]

value=65

for i in range(2,-1,-1):
    for j in range(5,-1,-1):
        arr[j][i] = chr(value)
        value += 1

x,y= map(int,input().split())

print(arr[x][y])