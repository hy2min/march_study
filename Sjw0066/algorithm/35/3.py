import heapq

N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
heap=[]
for i in range(N):
    for j in range(N):
        if arr[i][j] :
            heapq.heappush(heap,(arr[i][j],i,j))
direct_y=[0,0,1,-1]
direct_x=[1,-1,0,0]
visited=[[0]*N for _ in range(N)]
cnt=0
while heap:
    cnt+=1
    val,y,x=heapq.heappop(heap)

    if val==cnt:
        visited[y][x] = 1
        for i in range(4):
            dy=direct_y[i] + y
            dx=direct_x[i] + x
            if dy<0 or dx<0 or dy>N-1 or dx>N-1:continue
            if visited[dy][dx]==1:continue
            visited[dy][dx]=1
            heap.remove((arr[dy][dx],dy,dx))
            heapq.heapify(heap)
    else:
        heapq.heappush(heap,(val,y,x))
print(f'{cnt}초')

