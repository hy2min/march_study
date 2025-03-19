from collections import deque
S = int(input())
D = int(input())
def bfs(start):
    q = deque([(start, 0)])
    visited = set([start])
    while q:
        num, cnt = q.popleft()
        if num == D:
            return cnt
        for i in range(4):
            if i == 0:
                nxt = num // 2
                if nxt > 1e5:continue
                if nxt in visited: continue
                visited.add(nxt)
                q.append((nxt, cnt + 1))
            elif i == 1:
                nxt = num * 2
                if nxt > 1e5: continue
                if nxt in visited: continue
                visited.add(nxt)
                q.append((nxt, cnt + 1))
            elif i == 2:
                nxt = num + 1
                if nxt > 1e5: continue
                if nxt in visited: continue
                visited.add(nxt)
                q.append((nxt, cnt + 1))
            else:
                nxt = num - 1
                if nxt < 0: continue
                if nxt in visited: continue
                visited.add(nxt)
                q.append((nxt, cnt + 1))

print(bfs(S))

