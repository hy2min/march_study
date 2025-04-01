import sys
sys.stdin=open('input.txt','r')

# # 내 풀이
# n = int(input())
# arr = list(map(int, input().split()))
# lst = []
#
# for i in range(n-3):
#     lst.append(sum(arr[i:i+4]))
# print(min(lst))

# Sliding window 사용
n = int(input())
arr = list(map(int, input().split()))

# 처음 4개 숫자의 합
Sum = 0
for i in range(4):
    Sum += arr[i]

Min = Sum
# 옆으로 가면서 합 중 최소값 구하기
for i in range(n-4):
    Sum += arr[i+4]
    Sum -= arr[i]
    if Min > Sum:
        Min = Sum
print(Min)