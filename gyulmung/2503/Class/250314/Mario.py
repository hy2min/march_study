import sys
sys.stdin = open('input.txt','r')

def mario(level):
    if level >= n - 1:  # 마지막 위치 도착 시, 해당 위치 점수를 반환
        return 0
    if dp[level] != -sys.maxsize:  # 이미 계산한 경우
        return dp[level]

    # 이동 가능한 경우의 점수 계산
    jump_2 = arr[level + 2] + mario(level + 2) if level + 2 < n else float('-inf')
    jump_7 = arr[level + 7] + mario(level + 7) if level + 7 < n else float('-inf')

    # 최댓값 선택
    dp[level] = max(jump_2, jump_7)
    return dp[level]

n = int(input())
arr = list(map(int, input().split()))

dp = [-sys.maxsize] * n  # DP 배열 초기화 (최솟값으로 설정)
print(mario(0) + arr[0])  # 시작점도 포함해야 하므로 arr[0] 추가