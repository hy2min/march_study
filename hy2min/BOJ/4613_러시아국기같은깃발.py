t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    
    mx = 0
    # i,j 세영역으로 나누기
    for i in range(n-2):
        for j in range(i+1, n-1):
            cnt = 0
            for s in range(i+1):
                cnt += arr[s].count('W')
            for s in range(i+1,j+1):
                cnt += arr[s].count('B')
            for s in range(j+1,n):
                cnt += arr[s].count('R')
            mx = max(cnt, mx)
    print(f'#{tc} {n*m - mx}')