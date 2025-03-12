n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
for _ in range(k):
       arr_t = [[0] * n for _ in range(n)]
       for i in range(n):
              for j in range(n):
                     arr_t[j][n-i-1] = arr[i][j]
       arr = [row[:] for row in arr_t]

for i in arr:
       print(*i)
