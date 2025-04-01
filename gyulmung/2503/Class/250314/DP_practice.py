arr=[[0,5,3,6,8],
     [1,4,2,9,1],
     [6,9,1,7,7],
     [8,5,4,1,0]]

directy = [0, 1]
directx = [1, 0]
dp = [[0]*5 for _ in range(4)]

for i in range(1,4):
    dp[i][0] = dp[i-1][0]+arr[i][0]
for i in range(1,5):
    dp[0][i] = dp[0][i-1] + arr[0][i]

for i in range(1,4):
    for j in range(1, 5):
        dp[i][j] = min(dp[i-1][j]+arr[i][j],dp[i][j-1]+arr[i][j])
print(dp[3][4])