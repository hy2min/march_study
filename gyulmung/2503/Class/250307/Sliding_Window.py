# Sliding Window

# M개의 정수를 입력
# 연속된 n개의 정수의 합이 최대일 때 그 구간은 언제일까요?

import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
arr = list(map(int, input().split()))
Sum = 0
for i in range(m):  # 첫 m개 구간의 합 구하기
    Sum += arr[i]

Max = Sum
for i in range(n - m):
    Sum += arr[i + m]  # 오른쪽값 더하고
    Sum -= arr[i]  # 왼쪽값 빼기
    if Sum > Max: Max = Sum  # 맥스값 갱신
print(Max)

# 내 코드
# from collections import deque
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# q = deque()
#
# for i in range(M):
#     q.append(arr[i])
# cnt = 0
# Max = -1
# Maxidx = 0
#
# while 1:
#     if cnt+M == N:
#         break
#     if Max < sum(q):
#         Max = sum(q)
#         Maxidx = cnt
#     q.popleft()
#     q.append(arr[cnt+M])
#     cnt += 1
# print(Max)