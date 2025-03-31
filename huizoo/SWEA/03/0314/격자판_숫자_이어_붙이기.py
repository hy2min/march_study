d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    num = set()
    arr2 = []
    for i in range(4):
        for j in range(4):
            arr2.append((i, j, 1, arr[i][j]))

    while arr2:
        y, x, cnt, now = arr2.pop()
        if cnt >= 7:
            num.add(now)
            continue
        for dy, dx in d:
            ny, nx = dy+y, dx+x
            if ny<0 or nx<0 or ny>=4 or nx>=4: continue
            arr2.append((ny, nx, cnt+1, now*10+arr[ny][nx]))

    print(f'#{tc} {len(num)}')