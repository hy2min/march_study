from collections import deque

x,y=map(int,input().split())
q=deque()
n=int(input())
arr=[list(map(int,input().split()))for _ in range(n)]
tired=[[21e8]*n for _ in range(n)]
tired[x][y]=arr[x][y]
dirx=[1,-1,0,0]
diry=[0,0,1,-1]
q.append((x,y))
while q:
    (x1,y1)=q.popleft()
    for i in range(4):
        dx=x1+dirx[i]
        dy=y1+diry[i]
        if dx<0 or dy<0 or dx>n-1 or dy>n-1: continue
        if arr[dx][dy]==-1: continue
        if tired[dx][dy]>tired[x1][y1]+arr[dx][dy]:
            tired[dx][dy]=tired[x1][y1]+arr[dx][dy]
            q.append((dx,dy))
Max=-21e8
for i in range(n):
    for z in range(n):
        if tired[i][z]==21e8: continue
        Max=max(Max,tired[i][z])
print(Max)