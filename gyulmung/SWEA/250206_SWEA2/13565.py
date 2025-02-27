import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test in range(1, T+1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    gas = [0]*N
    for i in range(M):
        gas[arr[i]] = 1
    gas_cnt = 0
    p_bus = 0
    while True:
        gas_cnt += 1
        next_bus = 0
        for j in range(1, K+1):
            if p_bus + j == N:
                next_bus = 0
                p_bus += j
                break
            elif gas[p_bus + j] == 1:
                next_bus = max(next_bus, j)
        if p_bus == N:
            gas_cnt -= 1
            break
        elif p_bus == p_bus + next_bus:
            gas_cnt = 0
            break
        p_bus += next_bus

    print(f'#{test} {gas_cnt}')