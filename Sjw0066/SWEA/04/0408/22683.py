import heapq
T=int(input())

for tc in range(1,T+1):
    N,K = map(int,input().split())
    arr = [list(input()) for _ in range(N)]
    result=[[[21e8]*(K+1) for _ in range(N)]for _ in range(N)]
    commands=['R','L','A']
    direct_y=[-1,0,1,0]
    direct_x=[0,1,0,-1]
    steps=[
        [0, 1, 2, 1],
        [1, 0, 1, 2],
        [2, 1, 0, 1],
        [1, 2, 1, 0],
    ]
    direct=0
    st_y=0
    st_x=0
    ed_y = 0
    ed_x = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                st_y=i
                st_x=j
            if arr[i][j] == 'Y':
                ed_y=i
                ed_x=j
    result[st_y][st_x][K] = 0

    heap=[]
    heapq.heappush(heap,(0,st_y,st_x,direct,K))

    while heap:
        cnt,now_y,now_x,d_idx,tree=heapq.heappop(heap)

        if arr[now_y][now_x] == 'Y':
            break

        for i in range(4):
            dy = direct_y[i] + now_y
            dx = direct_x[i] + now_x
            if dy>N-1 or dy<0 or dx>N-1 or dx<0 : continue
            if arr[dy][dx] == 'T' and tree == 0 : continue
            step = cnt+steps[d_idx][i]+1
            if arr[dy][dx] == 'T' :
                if result[dy][dx][tree-1]>step:
                    result[dy][dx][tree-1] = step
                    heapq.heappush(heap,(step,dy,dx,i,tree-1))
            else:

                if result[dy][dx][tree] > step:
                    result[dy][dx][tree] = step
                    heapq.heappush(heap,(step,dy,dx,i,tree))

    if min(result[ed_y][ed_x]) == 21e8:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {min(result[ed_y][ed_x])}')
