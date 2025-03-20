# 외판원 순회
import sys
input = sys.stdin.readline


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr2 = [i for i in range(N)]


memo = dict()

for i in range(N):
    for j in range(N):
        if arr[i][j]:
            # 마지막 방문한 곳이 현재 i라면 그곳에 j 가는 경우 추가
            memo[i]