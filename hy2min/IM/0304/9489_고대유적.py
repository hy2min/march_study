def cnt_structure(n,m,arr):    
    max_cnt = 0
    for i in range(n):
        cnt = 0
        for j in range(m):
            if arr[i][j] == 1:
                cnt += 1
                max_cnt = max(max_cnt,cnt)
            else:
                cnt = 0
    return max_cnt

t = int(input())

for tc in range(1, t+1):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    arr_t = list(zip(*arr))

    ans = max(cnt_structure(n,m,arr), cnt_structure(m,n,arr_t))
    print(f'#{tc} {ans}')