N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
for _ in range(K):
    arr = list(zip(*arr))
    for i in range(N):
        arr[i] = arr[i][::-1]
for row in arr:
    print(*row)
