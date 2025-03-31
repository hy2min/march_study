T=10

for tc in range(1,T+1):
    N=int(input())
    tree=[0]*(N+1)
    connect_lst=[[] for _ in range(N+1)]
    simbole=['+','-','/','*']
    answer=0
    for i in range(N):
        lst=list(map(str,input().split()))
        if len(lst) == 4:
            tree[int(lst[0])] = lst[1]
            connect_lst[int(lst[0])].append(int(lst[2]))
            connect_lst[int(lst[0])].append(int(lst[3]))
        else:
            tree[int(lst[0])] = int(lst[1])

    for i in range(N,0,-1):
        if tree[i] in simbole:
            if tree[i] == '+':
                tree[i] = tree[connect_lst[i][0]] + tree[connect_lst[i][1]]
            elif tree[i] == '-':
                tree[i] = tree[connect_lst[i][0]] - tree[connect_lst[i][1]]
            elif tree[i] == '/':
                tree[i] = tree[connect_lst[i][0]] / tree[connect_lst[i][1]]
            elif tree[i] == '*':
                tree[i] = tree[connect_lst[i][0]] * tree[connect_lst[i][1]]

    print(f'#{tc} {int(tree[1])}')

