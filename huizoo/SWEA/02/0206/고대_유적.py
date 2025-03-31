T = int(input())
for tc in range(1, T+1) : 
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    longest = 0
    for i in range(N) : 
        length = 0
        for j in range(M) : 
            if arr[i][j] == 1 :
                length += 1
            elif longest < length : 
                longest = length
                length = 0
        if longest < length: 
            longest = length
    for j in range(M) :
        length = 0 
        for i in range(N) : 
            if arr[i][j] == 1 : 
                length += 1
            elif longest < length : 
                longest = length
                length = 0
        if longest < length: 
            longest = length
    print(f'#{tc} {longest}')
                
