import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
Sum = 0
for i in range(1, N+1):
    Sum += arr.pop() * i
print(Sum)

# import heapq, sys
# input = sys.stdin.readline
#
# N = int(input())
# arr = list(map(int, input().split()))
# heapq.heapify(arr)
# Sum = 0
# now = 0
# for i in range(N):
#     now += heapq.heappop(arr)
#     Sum += now
# print(Sum)