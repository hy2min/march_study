T = int(input())
for tc in range(1, T+1) :
    N = int(input())
    busstop = [0] * 5001

    for i in range(N) :
        a, b = map(int, input().split())
        for j in range(a, b+1) :
            busstop[j] += 1

    P = int(input())
    bus = []
    for i in range(P) :
        C = int(input())
        bus.append(busstop[C])

    print(f'#{tc} {" ".join(map(str, bus))}')