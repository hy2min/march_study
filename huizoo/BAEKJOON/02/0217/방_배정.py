N, K = map(int, input().split())
arr = [[0]*2 for _ in range(6)]
for _ in range(N):
    a, b = map(int, input().split())
    b -= 1
    arr[b][a] += 1
cnt = 0
for i in range(6):
    for j in range(2):
       cnt += (arr[i][j]-1)//K+1
print(cnt)