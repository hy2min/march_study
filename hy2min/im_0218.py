n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

d_y = [1,-1,0,0]
d_x = [0,0,-1,1]

def dfs(y,x,num,cnt):


    for i in range(4):
        num = arr[y][x]
        dy = y + d_y[i]
        dx = x + d_x[i]
        if dy<0 or dx<0 or dy>=n or dx>=n:
            continue
        if num < arr[dy][dx]:
            num = arr[dy][dx]
