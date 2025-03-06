t = int(input())
for tc in range(1, t+1):
    N = int(input())
    dat = [0]*10
    k = 0
    ans = 0
    while 0 in dat:
        k += 1
        ans = k*N
        for i in str(k*N):
            dat[int(i)] += 1
    print(f'#{tc} {ans}')