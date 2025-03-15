def postorder(x):
    if x >= N+1: return 0
    elif x >= N//2+1: return arr[x]
    elif x >= 0: return postorder(2*x) + postorder(2*x+1)

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = [0]*(N+1)
    for _ in range(M):
        idx, value = map(int, input().split())
        arr[idx] = value
    print(f'#{tc} {postorder(L)}')