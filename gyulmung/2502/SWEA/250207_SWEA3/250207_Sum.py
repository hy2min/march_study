test_case = 10
for tc in range(1, test_case + 1)
    ans = 0
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]
    Sum = [0]*202

    for i in range(100):
        for j in range(100):
            Sum[i] += lst[i][j]
            Sum[i + 100] += lst[i][j]
        Sum[200] += lst[i][i]
        Sum[201] += lst[i][99-i]

    ans = max(Sum)
    print(f'#{tc} {ans}')