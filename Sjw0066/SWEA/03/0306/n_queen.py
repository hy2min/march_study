import copy
T=int(input())

def queen(y,x):
    global arr

    if arr[y][x] == 1:
        return False

    for i in range(9):
        for j in range(1,N):
            dy=direct_y[i]*j+y
            dx=direct_x[i]*j+x
            if dy>N-1 or dy<0 or dx>N-1 or dx<0:break
            if arr[dy][dx] == 1: continue
            arr[dy][dx] = 1

    return True

def n_queen(level):
    global cnt,arr

    if level==N:
        cnt+=1
        return

    temp = copy.deepcopy(arr)

    for i in range(N):
        if arr[level][i] == 1: continue
        if used[i] == 1: continue
        if queen(level,i) :
            used[i] = 1
            n_queen(level+1)
            used[i] = 0
            arr=copy.deepcopy(temp)
        else:
            continue




for tc in range(1,T+1):
    N=int(input())
    arr=[[0]*N for _ in range(N)]
    direct_y=[-1,-1,-1,0,0,0,1,1,1]
    direct_x=[-1,0,1,-1,1,0,-1,0,1]
    cnt=0
    used=[0]*N
    n_queen(0)

    print(f'#{tc} {cnt}')