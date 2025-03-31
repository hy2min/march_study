def findboss(member):
    if arr[member] == member:
        return member
    ret = findboss(arr[member])
    arr[member] = ret
    return ret

def union(a, b):
    bossa, bossb = findboss(a), findboss(b)

    if bossa == bossb:
        return
    arr[bossb] = bossa
t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())

    arr = [i for i in range(n+1)]
    papers = list(map(int, input().split()))
    for i in range(m):
        union(papers[i*2], papers[i*2+1])

    for i in range(1, n+1):
        findboss(i)

    ans = set(arr[1:])
    print(f'#{tc} {len(ans)}')