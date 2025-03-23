T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    left = [0]*(N+1)
    right = [0]*(N+1)
    for i in range(1, N//2 + 1):
        left[i] = 2*i
        right[i] = 2*i+1
    if N % 2 == 0:
        right[N//2] = 0

    arr = [0]*(N+1)
    for _ in range(M):
        node, value = map(int, input().split())
        arr[node] = value
    Sum = 0
    def bst(x):
        global Sum
        if x:
            bst(left[x])
            bst(right[x])
            if x == L:
                return
            else:
                Sum += arr[x]

    bst(L)
    print(f'#{tc} {Sum}')