def move(x):
    cnt = 2
    for i in range(x + 1, n ** 2 + 1):
        if dat[i]:
            cnt += 1
        else:
            return cnt
    return cnt

d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = tuple(tuple(map(int, input().split())) for _ in range(n))
    dat = [0]*(n**2+1)
    for i in range(n):
        for j in range(n):
            now = arr[i][j]
            for dy, dx in d:
                ny, nx = i+dy, j+dx
                if ny<0 or nx<0 or ny>=n or nx>=n: continue
                if arr[ny][nx] == now + 1:
                    dat[now] = 1
                    break

    num, cnt = 0, 0
    for i in range(1, n**2+1):
        if dat[i]:
            ret = move(i)
            if cnt < ret:
                num = i
                cnt = ret

    print(f'#{tc} {num} {cnt}')