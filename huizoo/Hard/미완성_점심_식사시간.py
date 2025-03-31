t = int(input())
for tc in range(1, t+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = []
    s = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                p.append([i, j])
            if arr[i][j] >= 2:
                s.append([i, j, arr[i][j]])
    t = []
    for y1, x1 in p:
        tt = 50
        ss = 0
        for y2, x2, stair_time in s:
            ttt = abs(y1 - y2) + abs(x1 - x2) + stair_time
            if tt > ttt:
                tt = ttt
                ss = stair_time
        t.append([ss, tt])
    ans = 0
    if len(s) == 1:
        for tt, ss in t:
