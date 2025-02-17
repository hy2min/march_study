T = int(input())
for idx in range(T):
    N = int(input())
    sheep = set(str(N))
    cnt = 0
    times = 1
    while True:
        if len(sheep) == 10:
            break
        times += 1
        nw = N * times
        sheep.update(str(N*times))
    print(times)


