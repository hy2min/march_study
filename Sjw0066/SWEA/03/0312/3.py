T=int(input())

def get_result(lst1):
    ret=int(''.join(lst1))
    return ret





def dfs(lst1,level):
    global Max

    if level==int(N):
        ret=get_result(lst1)
        if Max<ret:
            Max=ret
        return

    temp = lst1[:]
    if temp in visited:
        return
    visited.append(temp)

    for i in range(len(lst1)-1):
        for j in range(i+1,len(lst1)):
            lst1[i] , lst1[j] = lst1[j] , lst1[i]
            dfs(lst1,level+1)
            lst1[i], lst1[j] = lst1[j], lst1[i]

for tc in range(1,T+1):
    input1, N = input().split()
    lst=list(input1)
    Max=-21e8
    visited = []
    dfs(lst,0)

    print(f'#{tc} {Max}')
