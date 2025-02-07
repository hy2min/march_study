for tc in range(1, 11) :
    n = int(input())
    ans = 0
    arr = [list(map(int, input().split())) for _ in range(100)]
    total = [0]*202
    for i in range(100) :
        for j in range(100) :
            total[i] += arr[i][j]
            total[100+i] += arr[j][i]
        total[200] = arr[i][i]
        total[201] = arr[i][-1-i]
    ans=max(total)
    print(f'#{n} {ans}')