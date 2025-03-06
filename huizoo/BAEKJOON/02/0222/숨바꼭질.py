from collections import deque

n, k = map(int, input().split())
def abc():
    time = [0]*100001
    q = deque()
    q.append(n)
    while q:
        now = q.popleft()
        if now == k:
            print(time[k])
            return
        for nxt in (now-1, now+1, now*2):
            if 0<=nxt<100001 and not time[nxt]:
                time[nxt] = time[now]+1
                q.append(nxt)
abc()