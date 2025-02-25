evid = [-1,0,0,1,2,4,4]
timeStamp = [8,3,5,6,8,9,10]

n = int(input())
path = [n]

def dfs(num):

    if num == 0:
        return

    path.append(evid[num])
    tmp = evid[num]
    dfs(tmp)

dfs(n)
N = len(path)
for i in range(N):
    if i == 0:
        print(f"{path[N-1-i]}번index(출발)")
    else:
        print(f"{path[N-1-i]}번index({timeStamp[path[N-1-i]]}시)")