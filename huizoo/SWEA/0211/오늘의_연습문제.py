T = int(input())
for tc in range(1, T+1) : 
    N, M = map(int, input().split())
    rock = list(map(int, input().split()))
    dx = [-1, 1]
    for _ in range(M) : 
        I, J = map(int, input().split())
        I_index = I-1
        for i in range(1, J+1) : 
            left, right = I_index + dx[0]*i, I_index + dx[1]*i
            if left < 0 or right >= N : 
                break
            elif rock[left] == rock[right] : 
                if rock[left] == 1 : 
                    rock[left], rock[right] = 0, 0
                else : 
                    rock[left], rock[right] = 1, 1

    print(f'#{tc}', *rock)
