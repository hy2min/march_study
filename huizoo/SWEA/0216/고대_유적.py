def abc(lst, y, x):
    global Max
    for i in range(y):
        for j in range(x):
            if lst[i][j]:
                length = 1
                for k in range(j+1, x):
                    if lst[i][k] == 1:
                        length += 1
                    else:
                        break
                if Max < length:
                    Max = length

t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr2 = list(zip(*arr))
    Max = 0
    abc(arr, N, M)
    abc(arr2, M, N)
    print(f'#{tc} {Max}')