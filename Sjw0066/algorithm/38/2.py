from collections import deque
arr=[list(map(int,input().split())) for _ in range(4)]

direct_y=[0,0,1,-1]
direct_x=[1,-1,0,0]
Max=-21e8
answer=0
def bfs(y,x,target):
    cnt=0
    q=deque()
    visited = [[0] * 9 for _ in range(4)]
    visited[y][x] = 1
    q.append((y,x))

    while q:
        yy,xx=q.popleft()
        cnt += 1
        for i in range(4):
            dy=yy+direct_y[i]
            dx=xx+direct_x[i]
            if dy<0 or dx<0 or dy>3 or dx>8:continue
            if visited[dy][dx] == 1:continue
            if arr[dy][dx] != target : continue
            visited[dy][dx] = 1
            q.append((dy,dx))

    return cnt

for i in range(10):
    for j in range(4):
        for k in range(9):
            if arr[j][k] == i:
                ret=bfs(j,k,i)
                if Max<ret:
                    Max=ret
                    answer=Max*i

print(answer)