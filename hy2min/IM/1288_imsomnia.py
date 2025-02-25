T = int(input())
for idx in range(T):
    N = int(input())
    sheep = set()

    times = 0
    while len(sheep) < 10:
        times += 1
        current_number = N * times
        sheep.update(str(current_number))
    print(f'#{idx+1} {current_number}')


