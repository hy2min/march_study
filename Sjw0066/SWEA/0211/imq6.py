T= int(input())


def check_five(y, x, d, cnt):
    global result
    if cnt == 5:
        result=1
        return
    dy = direct_y[d] + y
    dx = dircet_x[d] + x

    if dy < 0 or dy > N - 1 or dx < 0 or dx > N - 1 or arr[dy][dx] != 'o':
        return
    check_five(dy, dx, d, cnt + 1)

for tc in range(1, T + 1):
    N=int(input())
    direct_y=[1,1,1,0,0,-1,-1,-1]
    dircet_x=[1,0,-1,1,-1,1,0,-1]
    arr=[list(input()) for _ in range(N)]
    result=0

    for i in range(N):
        for j in range(N):

            if arr[i][j] == 'o':
                for k in range(8):
                    check_five(i,j,k,1)

                if result:
                    break
            if result:
                break
        if result:
            break

    if result:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')
