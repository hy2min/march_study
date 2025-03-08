n = int(input())
Map = [0] + list(map(int, input().split()))

dp = [0] + [-21e8]*n


ans = -21e8

for i in range(n+1):
    if dp[i] == -21e8:
        continue
    for jump in [2, 7]:
        nxt = i + jump
        if nxt <= n:
            dp[nxt] = max(dp[nxt], dp[i] + Map[nxt])
        else:
            ans = max(ans, dp[i])

print(ans)


# def jump(start, Sum):
#     global Max
#     if start <= N:
#         Sum += map_info[start]
#     if start >= N:
#         if Max<Sum:
#             Max = Sum
#         return
#     for i in [2, 7]:
#         jump(start+i, Sum)


# N = int(input())
# map_info = [0]+list(map(int, input().split()))
# Max = -21e8
# jump(0, 0)
# print(Max)