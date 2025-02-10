for idx in range(10):
    n = int(input())
    builings = list(map(int, input().split()))
    cnt_builing = 0
    for i in range(2,n-2):
        max_floor = max(builings[i-2], builings[i-1], builings[i+1], builings[i+2])

        if builings[i] > max_floor:
            cnt_builing += builings[i] - max_floor

    print(f'#{idx+1} {cnt_builing}')
