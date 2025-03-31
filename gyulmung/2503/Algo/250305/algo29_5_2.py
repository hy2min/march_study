evid = [-1, 0, 0, 1, 2, 4, 4]
timeStamp = [8, 3, 5, 6, 8, 9, 10]

N = int(input())
def dfs(now):
    if now == 0:
        print(f'{now}번index(출발)')
        return

    dfs(evid[now])
    print(f'{now}번index({timeStamp[now]}시)')

dfs(N)