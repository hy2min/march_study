T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Max = 0
    used_global = [0]*24
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x: (x[0], x[1]))
    def dfs(time, cnt, idx, used):
        global Max
        if time == 24 or idx == N:
            Max = max(Max, cnt)
            return
        for i in range(idx, N):
            start, end = arr[i]
            if used[start]: continue
            flag = 0
            used2 = used[:]
            for j in range(start, end):
                if used2[j]:
                    flag = 1
                    break
                used2[j] = 1
            if flag:
                continue
            else:
                dfs(end, cnt+1, i+1, used2)

        return

    dfs(0, 0, 0, used_global)

    print(f'#{tc} {Max}')