# import sys
# sys.stdin = open("input.txt","r")
import heapq

name = []
a = ord('A')
N = int(input())
cnt = 0
while cnt < N:
    name.append(chr(a))
    a += 1
    cnt += 1

arr = [list(map(int,input().split())) for _ in range(N)]
heap = []
for i in range(N):
    for j in range(N):
        heapq.heappush(heap,((-arr[i][j],(i,j)),(arr[i][j],(i,j))))

for _ in range(3):
    value,(st,ed) = heapq.heappop(heap)[1]
    print(f"{name[st]}-{name[ed]} {value}")