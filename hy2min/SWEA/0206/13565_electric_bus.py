T = int(input())
    K, N, M - map(int, input().split())
    charge_point = list(map(int, input().split()))
    bus_stop = [0] * N
    charge_cnt = 0
    for i in charge_point:
        bus_stop[i] = 1
    for i in range(N//K):
        if 1 in bus_stop[K*i:K*(i+1) +1]:
            charge_cnt += 1
    if
