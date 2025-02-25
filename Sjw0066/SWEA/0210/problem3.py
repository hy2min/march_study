T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    bus_nosun = []
    for i in range(N):
        a, b = map(int, input().split())
        bus_nosun.append([a, b])

    P = int(input())
    target_stop = []
    for i in range(P):
        bus_stop = int(input())
        target_stop.append(bus_stop)

    dat = [0] * 5001  # 버스 정류장 총 개수,번호

    # a~b 까지의 정류장에 들리는 노선만큼 +1
    for i in range(len(bus_nosun)):
        for j in range(bus_nosun[i][0], bus_nosun[i][1] + 1):
            dat[j] += 1

    print(f'#{tc}', end=" ")
    for i in range(P):
        print(dat[target_stop[i]], end=" ")
    print()
