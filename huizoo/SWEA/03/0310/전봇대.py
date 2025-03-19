t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = []
    cnt = 0
    for i in range(n):
        a, b = map(int, input().split())
        for c, d in arr:
            if a > c and b < d:
                cnt += 1
            elif a < c and b > d:
                cnt += 1
        arr.append((a, b) )
    print(f'#{tc} {cnt}')