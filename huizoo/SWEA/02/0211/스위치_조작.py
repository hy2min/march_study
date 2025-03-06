T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if a[i] != b[i]:
            cnt += 1
            for j in range(i, N):
                a[j] = (a[j] + 1) % 2
    print(f'#{tc} {cnt}')