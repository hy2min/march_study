t = int(input())
for tc in range(1, t+1):
    l,p,c = map(int, input().split())

    cnt = 0
    n = l

    while n < p:
        n *= c
        cnt += 1

    ans = 0
    while (1<< ans) < cnt:
        ans += 1

    print(f'#{tc} {ans}')