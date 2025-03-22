from copy import deepcopy
N, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
tmp = deepcopy(arr)

for _ in range(K):
    for i in range(N):
        for j in range(N):
            arr[j][N-1-i] = tmp[i][j]
    tmp = deepcopy(arr)

for i in range(N):
    print(*arr[i])