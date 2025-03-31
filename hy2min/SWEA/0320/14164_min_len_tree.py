def findboss(m):
    if uf[m] == m:
        return m
    ret = findboss(uf[m])
    return ret

def union(a, b):
    bossa, bossb = findboss(a), findboss(b)
    if bossa == bossb:
        return
    if bossa < bossb:
        uf[bossb] = bossa
    else:
        uf[bossa] = bossb

t = int(input())
for tc in range(1, t+1):
    v, e = map(int, input().split())  # 정점 간선
    arr = []
    uf = list(range(v+1))  # union_find boss 값 저장할 배열
    total = 0

    for _ in range(e):
        start, end, cost = map(int, input().split())
        arr.append((cost, start, end))

    arr.sort()

    for i in range(e):
        cost, a, b = arr[i]
        if findboss(a) != findboss(b):
            union(a, b)
            total += cost

    print(f'#{tc} {total}')