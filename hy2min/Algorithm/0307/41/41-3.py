def dfs(t, cnt):
    global min_cnt
    
    if t <0 or cnt > min_cnt:
        return
    if t == 0:
        min_cnt = min(min_cnt,cnt)
        return
    

    for i in arr:
        dfs(t - i, cnt + 1)

t, n = map(int, input().split())
arr = list(map(int, input().split()))
min_cnt = 21e8
dfs(t,0)
print(min_cnt)

    # DP로 풀어야 함