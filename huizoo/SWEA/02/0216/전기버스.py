t = int(input())
for tc in range(1, t+1):
    K, N, M = map(int, input().split())
    bus = list(map(int, input().split()))
    bus.insert(0, 0)
    bus.append(N)
    i = 0
    loc = 0
    cnt = 0
    flag = 0
    while i < M+2 and bus[i]+K < N:
        for j in range(i+1, M+2):
            if j == i+1:
                if bus[j] > bus[i]+K:
                    flag = 1
                    break
                else:
                    loc = j
            elif bus[j] <= bus[i]+K:
                loc = j
            else: break
        if flag: break
        cnt += 1
        i = loc


    if flag: print(f'#{tc} {0}')
    else: print(f'#{tc} {cnt}')