# import sys
# sys.stdin = open("input.txt","r")
import heapq

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
heap = []
for i in range(N):
    for j in range(i+1,N):
        if arr[i][j] > 0:
            heapq.heappush(heap,arr[i][j])

cnt = 0
while True:
    value = heapq.heappop(heap)
    value *= 2
    heapq.heappush(heap,value)
    cnt += 1
    if cnt == 10:
        print(f"{value}만원")
        break
