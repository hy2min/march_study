T=10

def inorder(now):

    if now>N:
        return

    inorder(now*2)
    print(tree[now],end="")
    inorder(now*2+1)

for tc in range(1,T+1):
    N=int(input())
    tree=[0]*(N+1)

    for i in range(N):
        lst=list(map(str,input().split()))
        tree[int(lst[0])] = lst[1]

    print(f'#{tc}',end=" ")
    inorder(1)
    print()