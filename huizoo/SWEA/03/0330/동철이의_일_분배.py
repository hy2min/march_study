import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dp = [0] * (1 << N)
    dp[0] = 1

    for mask in range(1 << N):
        i = bin(mask).count('1')
        if i >= N:
            continue
        for j in range(N):
            if not (mask & (1 << j)):
                nxt_mask = mask | (1 << j)
                dp[nxt_mask] = max(dp[nxt_mask], dp[mask]*arr[i][j]*0.01)

    ans = dp[(1 << N) - 1] * 100
    print(f'#{tc} {ans:6f}')

# T = int(input())
#
# for case_num in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     P = [[x / 100 for x in row] for row in arr]  # 퍼센트 -> 실수로 변환
#
#     dp = [0] * (1 << N)
#     dp[0] = 1
#
#     for mask in range(1 << N):
#         i = bin(mask).count('1')  # 현재 몇 명의 직원이 배정되었는지
#         if i >= N:
#             continue
#
#         for j in range(N):
#             if not (mask & (1 << j)):  # j번 일이 아직 배정되지 않았다면
#                 next_mask = mask | (1 << j)
#                 dp[next_mask] = max(dp[next_mask], dp[mask] * P[i][j])
#
#     result = dp[(1 << N) - 1] * 100  # 모든 일이 배정된 상태의 확률 * 100
#     print(f"#{case_num} {result:.6f}")