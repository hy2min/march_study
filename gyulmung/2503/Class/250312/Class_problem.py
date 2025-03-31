# Baekjoon 1715 카드 정렬하기

import sys
sys.stdin = open('input.txt', 'r')

# 내 풀이 - 틀렸습니다.
import heapq
n = int(input())
arr = []

for i in range(n):
    m = int(input())
    heapq.heappush(arr, m)

lst = []
for i in range(n):
    lst.append(heapq.heappop(arr))

Sum = 0
for i in range(n):
    Sum += lst[i]*(n-i)
print(Sum-lst[0])

# 강사님 풀이
# import heapq
# n=int(input())
# card=[]
# for i in range(n):
#     heapq.heappush(card,int(input()))
# answer=0
# while len(card)>1:
#     temp1=heapq.heappop(card)
#     temp2=heapq.heappop(card)
#     answer+=(temp1+temp2)
#     heapq.heappush(card,temp1+temp2)
# print(answer)