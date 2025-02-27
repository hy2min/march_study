arr = [
    [0, 0, 1, 0, 1, 1],
    [1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]
used = [0] * 6


def dfs(now, cnt):
    global Min
    global flag
    if now == B - 1:
        if cnt < Min:
            Min = cnt
        flag = 1

    for i in range(6):
        if arr[now][i] and used[i] == 0:
            used[i] = 1
            dfs(i, cnt + 1)
            used[i] = 0


A, B = map(int, input().split())
Min = 21e8
flag = 0
dfs(A - 1, 0)

if flag:
    print(Min)
else:
    print(0)

