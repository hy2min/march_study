# import sys
# sys.stdin = open("input.txt","r")
import heapq

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
heap = []
for i in range(N):
    for j in range(N):
        heapq.heappush(heap,(arr[i][j],i,j))

check_lst = [1] * (N ** 2 + 1)
dY = [0,0,0,1,-1]
dX = [0,1,-1,0,0]
cnt = 0

def bomb(Y,X):

    global cnt
    for i in range(5):
        dy = Y + dY[i]
        dx = X + dX[i]
        if dy < 0 or dy > N - 1 or dx < 0 or dx > N - 1: continue
        if visited[dy][dx] == 1: continue
        visited[dy][dx] = 1
        check_lst[arr[dy][dx]] = 0
        cnt += 1
    if cnt == N ** 2:
        return 1
    return 0

while heap:

    time,y,x = heapq.heappop(heap)
    if check_lst[time] == 0:
        continue
    flag = bomb(y,x)
    if flag:
        print(f"{time}초")
        break



