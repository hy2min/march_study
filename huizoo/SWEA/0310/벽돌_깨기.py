import copy
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(level, lst):
    global Min
    if level == N:
        cnt = 0
        for i in range(H):
            for j in range(W):
                if lst[i][j]:
                    cnt += 1
        Min = min(cnt, Min)
        return
    for j in range(W):
        flag = 0
        for i in range(H):
            if lst[i][j]:
                lst2 = copy.deepcopy(lst)
                if lst2[i][j] == 1:
                    lst2[i][j] = 0
                else:
                    lst2 = boom(i, j, lst2)
                    lst2 = down(lst2)
                dfs(level + 1, lst2)
                flag = 1
                break
        if not flag:
            dfs(level + 1, lst)

def boom(y, x, lst):
    queue = [(y, x, lst[y][x] - 1)]
    while queue:
        yy, xx, power = queue.pop()
        lst[yy][xx] = 0
        for dy, dx in d:
            for p in range(1, power+1):
                ny, nx = yy + dy * p, xx + dx * p
                if ny < 0 or nx < 0 or ny >= H or nx >= W: continue
                if lst[ny][nx] >= 1:
                    queue.append((ny, nx, lst[ny][nx]-1))
    return lst

def down(lst):
    for j in range(W):
        bottom = H - 1
        for i in range(H - 1, -1, -1):
            if lst[i][j]:
                lst[bottom][j], lst[i][j] = lst[i][j], lst[bottom][j]
                bottom -= 1
    return lst

t = int(input())
for tc in range(1, t+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    Min = 1e6
    dfs(0, arr)
    print(f'#{tc} {Min}')
