n = 4
grid = [list(map(int, input().split())) for _ in range(n)]

# dp 배열: 최소 누적 합
dp = [[0] * n for _ in range(n)]
# predecessor 배열: 각 셀의 바로 이전 좌표 저장 (없으면 None)
pre = [[None] * n for _ in range(n)]

dp[0][0] = grid[0][0]

# 첫 번째 행과 첫 번째 열은 따로 처리 (경로는 유일)
for j in range(1, n):
    dp[0][j] = dp[0][j-1] + grid[0][j]
    pre[0][j] = (0, j-1)
for i in range(1, n):
    dp[i][0] = dp[i-1][0] + grid[i][0]
    pre[i][0] = (i-1, 0)

# 나머지 셀에 대해 dp 채우기
for i in range(1, n):
    for j in range(1, n):
        # 위쪽과 왼쪽에서 오는 경우 중 최소 비용 선택
        if dp[i-1][j] < dp[i][j-1]:
            dp[i][j] = dp[i-1][j] + grid[i][j]
            pre[i][j] = (i-1, j)
        else:
            dp[i][j] = dp[i][j-1] + grid[i][j]
            pre[i][j] = (i, j-1)

# 목적지에서부터 시작하여 경로 복원 (backtracking)
path = []
i, j = n-1, n-1
while (i, j) is not None:
    path.append((i, j))
    prev = pre[i][j]
    if prev is None:
        break
    i, j = prev

# 경로를 시작점부터 출력하기 위해 reverse
path.reverse()
for coord in path:
    print(f'{coord[0]},{coord[1]}')
