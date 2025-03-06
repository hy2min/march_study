# 가로세로 공용
dy1 = [0, 0, 0, 0, 0]
dx1 = [-2, -1, 0, 1, 2]
# 대각선 공용
dy2 = [-2, -1, 0, 1, 2]
dx2 = [-2, -1, 0, 1, 2]

T = int(input())
for tc in range(1, T+1) : 
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    flag = False
    for y in range(N) : 
        for x in range(N) :
            if arr[y][x] == 'o' :
                # 가로 탐색 
                cnt1 = 0
                for i in range(5) : 
                    ny, nx = y+dy1[i], x+dx1[i]
                    if 0 <= ny < N and 0 <= nx < N : 
                        if arr[ny][nx] == 'o' : 
                            cnt1 += 1
                            
                # 세로 탐색
                cnt2 = 0
                for i in range(5) : 
                    ny, nx = y+dx1[i], x+dy1[i]
                    if 0 <= ny < N and 0 <= nx < N : 
                        if arr[ny][nx] == 'o' : 
                            cnt2 += 1
                            
                # 대각선 \ 탐색
                cnt3 = 0
                for i in range(5) :
                    ny, nx = y+dy2[i], x+dx2[i]
                    if 0 <= ny < N and 0 <= nx < N : 
                        if arr[ny][nx] == 'o' : 
                            cnt3 += 1
                            
                # 대각선 / 탐색
                cnt4 = 0
                for i in range(5) : 
                    ny, nx = y+dy2[i], x+dx2[-i-1]
                    if 0 <= ny < N and 0 <= nx < N : 
                        if arr[ny][nx] == 'o' : 
                            cnt4 += 1
                if 5 in [cnt1, cnt2, cnt3, cnt4] : 
                    flag = True
        
    if flag:
        print(f'#{tc} YES')
    else : 
        print(f'#{tc} NO')