from collections import deque

S = int(input())
D = int(input())
q = deque()
q.append((S,0))
ans = 1e10
used = [0] * 100001
used[S] = 1

while q:

    now, cnt = q.popleft()
    if now == D:
        ans = min(ans,cnt)
    lst = [now-1,now+1,now//2,now*2]
    for i in range(4):
        if 0 <= lst[i] <= 100000 and used[lst[i]] == 0:
            used[lst[i]] = 1
            q.append((lst[i],cnt+1))

print(ans)