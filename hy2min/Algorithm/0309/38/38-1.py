from collections import deque

def bfs(s):
    visited = set()
    q = deque()
    q.append((s, 0))

    while q:
        channel, cnt = q.popleft()

        if channel == d:
            return cnt
        
        if channel in visited:
            continue
        visited.add(channel)

        if channel * 2 <= max_channel:
            q.append((channel*2,cnt+1))
        if channel // 2 <= max_channel:
            q.append((channel//2,cnt+1))
        if channel + 1 <= max_channel:
            q.append((channel+1,cnt+1))
        if channel - 1 <= max_channel:
            q.append((channel-1,cnt+1))

s = int(input())
d = int(input())

max_channel = 100000

print(bfs(s))
