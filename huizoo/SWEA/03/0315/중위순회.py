def inorder(x):
    if x > N: return
    info = arr[x]
    if len(info) > 1:
        inorder(int(info[1]))
        print(info[0], end='')
        if len(info) == 3:
            inorder(int(info[2]))
    else:
        print(info[0], end='')

for tc in range(1, 11):
    N = int(input())
    arr = [0]*(N+1)
    for _ in range(N):
        idx, *a = input().split()
        arr[int(idx)] = a
    print(f'#{tc} ', end='')
    inorder(1)
    print()