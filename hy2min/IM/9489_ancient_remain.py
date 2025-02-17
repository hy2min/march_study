def remain_length(data, N, M):
    max_cnt = 0
    for i in range(N):
        cnt = 0
        for j in range(M):
            if data[i][j] == 1:
                cnt += 1
                if cnt > max_cnt:
                    max_cnt = cnt
            else:
                cnt = 0
    return max_cnt

T = int(input())
for idx in range(T):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    data2 = list(zip(*data))


    res = max(remain_length(data, N, M), remain_length(data2, M, N))
    print(f'#{idx + 1} {res}')