T = 10
for test_case in range(1,T+1):
    ans = 0
    n = int(input())
    lst=[list(map(int,input().split())) for _ in range(100)]
    Sum = [0] * 202

    for i in range(100):
        for j in range(100):
            Sum[i] += lst[i][j]
            Sum[i+100] += lst[j][i]
        sum[200] = lst[i][i]
        sum[201] = lst[i][99-i]

    ans = max(lst)
    print(f"#{test_case} {ans}")