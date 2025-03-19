T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = [0]*(N+2)
    for _ in range(M):
        idx, value = map(int, input().split())
        arr[idx] = value
    for i in range(N//2, 0, -1):
        arr[i] = arr[2*i] + arr[2*i+1]
    print(f'#{tc} {arr[L]}')