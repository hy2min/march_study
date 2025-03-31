import sys
sys.stdin = open("input.txt","r")
import heapq

def dijkstra():

    heap = [(0,0,0)]    # cost, y, x

    while heap:

        cost, y, x = heapq.heappop(heap)

        if time[y][x] < cost:
            continue

        next_axis = [(y-1,x), (y+1,x), (y,x-1), (y,x+1)]
        next = [a for a in next_axis if 0 <= a[0] <= N-1 and 0 <= a[1] <= N-1]

        for dy, dx in next:
            if time[dy][dx] > cost + arr[dy][dx]:
                time[dy][dx] = cost + arr[dy][dx]
                heapq.heappush(heap, (cost+arr[dy][dx],dy,dx))

    return time[N-1][N-1]


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    inf = 21e8
    time = [[inf] * N for _ in range(N)]
    time[0][0] = 0
    ans = dijkstra()
    print(f"#{tc} {ans}")