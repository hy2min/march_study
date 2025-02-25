t = int(input())
for tc in range(1, t+1):
    N = int(input())
    arr = [[''] * 10 for _ in range(10)]
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        if color == 1:
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    arr[i][j] += 'r'
        else:
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    arr[i][j] += 'b'
    cnt = 0
    for i in range(10):
        for j in range(10):
            if 'rb' in arr[i][j] or 'br' in arr[i][j]:
                cnt += 1
    print(f'#{tc} {cnt}')