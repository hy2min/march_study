T=int(input())



def dfs(now):
    global flag

    if now == G :
        flag=1
        return

    visited[now] = 1
    for i in lst[now]:
        if visited[i] : continue
        dfs(i)




for tc in range(1,T+1):

    V,E=map(int,input().split())
    lst=[[] for _ in range(V+1)]
    for i in range(E):
        st,ed=map(int,input().split())
        lst[st].append(ed)

    S,G = map(int,input().split())
    flag=0
    visited=[0]*(V+1)
    dfs(S)

    if flag:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')



