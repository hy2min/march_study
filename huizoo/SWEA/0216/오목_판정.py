t = int(input())
for tc in range(1, t+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    found = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                cnt = 1
                if j+5 <= N:
                    if arr[i][j:j+5] == ['o']*5:
                        cnt = 5
                if i+5 <= N:
                    for k in range(1, 5):
                        if arr[i+k][j] == 'o':
                            cnt += 1
                if j+5 <= N and i+5 <= N:
                    for k in range(1, 5):
                        if arr[i+k][j+k] == 'o':
                            cnt += 1
                if j >= 4 and i+5 <= N:
                    for k in range(1, 5):
                        if arr[i+k][j-k] == 'o':
                            cnt += 1
                if cnt == 5:
                    found = 1
    if found:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')