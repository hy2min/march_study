T = int(input())
for tc in range(1, T+1):
    cost = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    Min = sum(arr) * cost[0]
    def dfs(month, Sum):
        global Min
        # 최소값의 초기값을 전부 1일권 구매했을 때의 가격으로 지정 후 가지치기
        if Sum > Min:
            return
        if month >= 12:
            Min = min(Min, Sum)
            return
        day = arr[month]
        if not day:
            dfs(month+1, Sum)
        else:
            for i in range(4):
                if i == 0:
                    dfs(month+1, Sum + day*cost[i])
                elif i == 1:
                    dfs(month+1, Sum + cost[i])
                elif i == 2:
                    dfs(month+3, Sum + cost[i])
                else:
                    dfs(month+12, Sum + cost[i])

    dfs(0, 0)
    print(f'#{tc} {Min}')