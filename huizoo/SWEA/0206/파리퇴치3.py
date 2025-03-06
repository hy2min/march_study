T = int(input())
for tc in range(1, T+1) : 
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]
    # + 모양 스프레이
    dy1 = [i for i in range(-M+1, M)] + [0]*(2*M-1)
    dy1.pop(-M)
    dx1 = [0]*(2*M-1) + [i for i in range(-M+1, M)]
    dx1.pop(-M)
    # x 모양 스프레이                
    dy2 = [i for i in range(-M+1, M)] + [i for i in range(M-1, -M, -1)]
    dy2.pop(-M)
    dx2 = [i for i in range(-M+1, M)] + [i for i in range(-M+1, M)]
    dx2.pop(-M)
    max_catch = 0
    
    for y in range(N) : 
        for x in range(N) : 
            # + 모양 스프레이
            catch = 0
            for i in range(4*M-3) : 
                ny, nx = y + dy1[i], x + dx1[i]
                if 0 <= ny < N and 0 <= nx < N : 
                    catch += flies[ny][nx]
            if max_catch < catch : 
                max_catch = catch
            # x 모양 스프레이
            catch = 0
            for i in range(4*M-3) : 
                ny, nx = y + dy2[i], x + dx2[i]
                if 0 <= ny < N and 0 <= nx < N : 
                    catch += flies[ny][nx]
            if max_catch < catch : 
                max_catch = catch

    print(f'#{tc} {max_catch}')