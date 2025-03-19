t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    cnt = 0
    used = [0]*n
    def abc(y):
        global cnt
        if y == n:
            cnt += 1
            return
        for x in range(n):
            if used[x]: continue
            flag2 = 1
            for i in range(-n, n+1):
                ny1, nx1 = y+i, x+i
                if 0<= ny1 < n and 0 <= nx1 < n:
                    if arr[ny1][nx1]:
                        flag2 = 0
                ny2, nx2 = y+i, x-i
                if 0<= ny2 < n and 0 <= nx2 < n:
                    if arr[ny2][nx2]:
                        flag2 = 0
            if flag2:
                arr[y][x] = 1
                used[x] = 1
                abc(y+1)
                arr[y][x] = 0
                used[x] = 0

    for i in range(n):
        arr[0][i] = 1
        used[i] = 1
        abc(1)
        arr[0][i] = 0
        used[i] = 0
    print(f'#{tc} {cnt}')