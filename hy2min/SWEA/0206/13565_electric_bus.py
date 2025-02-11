T = int(input())
for idx in range(T):
    K, N, M = map(int, input().split()) # 최대 이동 수, 종점(목표) 정류장, 충전기설치수
    charge_point = list(map(int, input().split())) # 충전 정류장 번호
    flag = 1
    for i in range(1,M):
        if charge_point[i]-charge_point[i-1] > K:
            flag = 0
    if flag == 1:
        cnt = 0
        moving = K
        while moving < N:
            if moving in charge_point:
                cnt += 1
                moving += K
            else:
                moving -= 1
    else:
        cnt = 0
    print(f'#{idx+1} {cnt}')


