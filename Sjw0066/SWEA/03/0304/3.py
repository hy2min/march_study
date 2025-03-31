T=int(input())

def inorder(now):#중위순회
    global val
    if now>N :
        return

    inorder(now*2) # 트리의 왼쪽 들어가기
    tree[now] = val # 트리가 더이상 들어가지 못하고 리턴하면 왼쪽-> 가운데-> 오른쪽 아래
    val += 1 # 순으로 1씩 증가시켜서 넣기
    inorder(now*2+1) # 트리의 오른쪽 들어가기

for tc in range(1,T+1):
    N=int(input())
    tree=[0]*(N+1)
    val = 1
    inorder(1)



    print(f'#{tc} {tree[1]} {tree[N//2]}')