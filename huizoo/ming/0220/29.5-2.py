def dfs(x):
    if x == 0:
        print('0번index(출발)')
        return
    dfs(evid[x])
    print(f'{x}번index({timeStamp[x]}시)')


idx = int(input())
evid = [-1,0,0,1,2,4,4]
timeStamp = [8,3,5,6,8,9,10]

dfs(idx)