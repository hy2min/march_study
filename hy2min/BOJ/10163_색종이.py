arr = [[0] * 1001 for _ in range(1001)]
n = int(input())
for num in range(n):
    y,x,width,height = map(int, input().split())
    for i in range(y,y+width):
        for j in range(x,x+height):
            arr[i][j] = num+1

for i in range(1,n+1):
    cnt = 0
    for lst in arr:
        cnt += lst.count(i)
    print(cnt)