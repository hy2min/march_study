def find_cross_sum(n,m,a,b):
    mx = -21e8
    for i in range(m-n+1):
        sm = 0
        for j in range(n):
            sm += a[j] * b[j+i]
        if sm > mx:
            mx = sm
    print(f'#{tc} {mx}')

t = int(input())
for tc in range(1, t+1):
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if n < m:
        find_cross_sum(n,m,a,b)
    else:
        find_cross_sum(m,n,b,a)