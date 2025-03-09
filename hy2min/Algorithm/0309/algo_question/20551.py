t = int(input())
for tc in range(1,t+1):
    a, b, c = map(int, input().split())
    cnt = 0
    while b >= c:
        b -= 1
        cnt += 1
    while a >= b:
        a -= 1
        cnt += 1
    if b == 0 or a == 0:
        cnt = -1
    print(f'#{tc} {cnt}')
