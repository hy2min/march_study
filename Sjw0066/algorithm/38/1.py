from collections import deque
S=int(input())
D=int(input())
cntt=0
visited=[0]*100000
answer=21e8
q=deque()
q.append((S,cntt))

while q:
    now,cnt=q.popleft()

    if now==D:
        print(cnt)
        break

    lst=[now//2,now*2,now+1,now-1]

    for i in lst:
        if i > 99999 or i<0 :continue
        if visited[i] == 1 : continue
        visited[i] = 1
        q.append((i,cnt+1))

