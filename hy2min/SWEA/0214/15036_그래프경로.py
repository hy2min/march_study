def dfs(s):
    if s == G:
        return 1

    for i in range(v):
        if arr[s][i] == 1:
            if not used[i]:
                used[i] = 1
                if dfs(i):
                    return 1
                used[i] = 0
    return 0

t = int(input())
for tc in range(1, t+1):
    v,e = map(int, input().split())
    arr = [[0]*v for _ in range(v)]

    for _ in range(e):
        s,g = map(int, input().split())
        s-=1
        g-=1
        arr[s][g] = 1

    S,G = map(int, input().split())
    S -= 1
    G -= 1

    used = [0] *v
    used[S] = 1
    

    ans = dfs(S)
    print(f'#{tc} {ans}')
