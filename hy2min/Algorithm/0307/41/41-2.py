# n = int(input())
# inf = -21e8
# arr = [0] + list(map(int,input().split())) + [0]*7
# dp = [[inf] * 2 for _ in range(len(arr))]
# dp[1] = [0,inf]
# dp[2] = [arr[2],inf]
# for i in range(2, len(arr)):
#     dp[i][0] = max(dp[i-2]) + arr[i]
#     if i >= 7:
#         dp[i][1] = max(dp[i-7]) + arr[i]
#
# print(*dp)
# print(max(dp[n:]))
#
inf = -21e8
n = int(input())
arr = [0] + list(map(int, input().split())) + [0]*10

dp = [inf] * len(arr)
dp[0]= 0
for i in range(2,9,2):
    dp[i] = dp[i-2] + arr[i]
dp[7] = arr[7]
for i in range(8, len(arr)):
    if i in [8, 10, 12]:
        continue
    dp[i] = arr[i] + max(dp[i-2], dp[i-7])

print(max(dp[n:]))