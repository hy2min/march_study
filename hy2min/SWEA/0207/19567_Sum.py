T = 10
for _ in range(T):
    N = int(input())
    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))
    max_sum = 0


    for i in range(100):
        part_sum = 0
        for j in range(100):
            part_sum += arr[j][j] # 좌우 대각선
        if part_sum > max_sum:
            max_sum = part_sum

    for i in range(100):
        part_sum = 0
        for j in range(100):
            part_sum += arr[j][99-j] # 우좌 대각선
        if part_sum > max_sum:
            max_sum = part_sum

    for i in range(100):
        part_sum = 0
        for j in range(100):
            part_sum += arr[i][j] # 행
        if part_sum > max_sum:
            max_sum = part_sum

    for i in range(100):
        part_sum = 0
        for j in range(100):
            part_sum += arr[j][i] # 열
        if part_sum > max_sum:
            max_sum = part_sum

    print(f'#{N} {max_sum}')
