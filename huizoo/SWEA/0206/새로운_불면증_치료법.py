def devide_num(num) :
    a = (num // 1000000) % 10
    b = (num // 100000) % 10
    c = (num // 10000) % 10
    d = (num // 1000) % 10
    e = (num // 100) % 10
    f = (num // 10) % 10 
    g = num % 10

    return [a, b, c, d, e, f, g]

T = int(input())
for tc in range(1, T+1) : 
    N = int(input())
    dat = [0]*10
    cnt = 0
    n = 1
    while 0 in dat : 
        ret = devide_num(N*n)
        while ret[0] == 0 : 
            ret.pop(0)
        for num in ret : 
            dat[num] += 1
        cnt += N
        n += 1
    print(f'#{tc} {cnt}')