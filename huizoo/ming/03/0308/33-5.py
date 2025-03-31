n= int(input())
arr = list(map(int, input().split()))
K = int(input())
friend = [[] for _ in range(n)]
visited = [0]*n
def abc(x):
    visited[x] = 1
    Sum = arr[x]
    cnt = 1
    for nxt in friend[x]:
        if not visited[nxt]:
            ret1, ret2 = abc(nxt)
            Sum += ret1
            cnt += ret2
    return Sum, cnt

for _ in range(K):
    a, b, c = input().split()
    b, c = ord(b) - 65, ord(c) - 65
    if a == 'war':
        nation1, nation2 = 0, 0
        cnt1, nation1 = abc(b)
        cnt2, nation2 = abc(c)
        if cnt1 > cnt2:
            n -= nation2
        else:
            n -= nation1
    else:
        friend[b].append(c)
        friend[c].append(b)

print(n)