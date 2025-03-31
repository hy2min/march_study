T=int(input())

def dfs(level,Sum):
    global Max

    if level==N:
        Max=max(Max,Sum)
        return

    power_a=lstA[level]
    power_b=lstB[level]

    if level>0:
        if path[level-1] == 'A':
            power_a=lstA[level]-P
        else:
            power_b=lstB[level]-P

    power=[power_a,power_b]

    for i in range(2):
        path[level] = name[i]
        dfs(level+1,Sum+power[i])

for tc in range(1,T+1):
    N,P = map(int,input().split())
    lstA=list(map(int,input().split()))
    lstB=list(map(int,input().split()))
    path=[0]*N
    name=['A','B']
    Max=-21e8
    dfs(0,0)
    print(f'#{tc} {Max}')
