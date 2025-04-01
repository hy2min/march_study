import sys
sys.stdin = open('input.txt','r')


# T = int(input())
# for test in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     Sum = 0
#     for i in range(N):
#         Max = 0
#         for j in range(i, N):
#             if arr[j] - arr[i] > 0 and Max < arr[j] - arr[i]:
#                 Max = arr[j] - arr[i]
#         Sum += Max
#     ans = Sum
#
#     print(f'#{test} {ans}')

# from collections import deque
#
# T = int(input())
# for test in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     q=[]
#     while 1:
#         a = arr.pop(0)
#         if not arr:
#             break
#         b = max(arr) - a
#         if b > 0:
#             q.append(b)
#     ans = sum(q)
#     print(f'#{test} {ans}')


T = int(input())
for test in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    Max = 0
    q = []

    for i in range(N - 1, -1, -1):
        if arr[i] > Max:
            Max = arr[i]
        else:
            q.append(Max - arr[i])

    ans = sum(q)
    print(f'#{test} {ans}')