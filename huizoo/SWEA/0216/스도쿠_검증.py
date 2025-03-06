t = int(input())
for tc in range(1, t+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    flag = 0
    for i in range(9):
        dat1 = [0]*10
        dat2 = [0]*10
        for j in range(9):
            dat1[arr[i][j]] += 1
            dat2[arr[j][i]] += 1
        if dat1.count(1) != 9 or dat2.count(1) != 9:
            flag = 1
    for i in range(0, 9, 3):
        dat3 = [0]*10
        for j in range(3):
            for k in range(3):
                dat3[arr[i+j][i+k]] += 1
        if dat3.count(1) != 9:
            flag = 1
    if flag:
        print(f'#{tc} {0}')
    else:
        print(f'#{tc} {1}')