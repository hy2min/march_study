T = int(input())
for tc in range(1, T+1) :
    N = int(input())
    arr = [['']*10 for _ in range(10)]
    for _ in range(N) :
        y1, x1, y2, x2, c = map(int, input().split())
        for i in range(y1, y2+1) :
            for j in range(x1, x2+1) :
                arr[i][j] += str(c)
    purple = 0
    for i in range(10) :
        for j in range(10) :
            if '1' in arr[i][j] and '2' in arr[i][j] :
                purple += 1

    print(f'#{tc} {purple}')
