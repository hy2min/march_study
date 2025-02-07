def kill_fly():
    kill = 0
    for y in range(M):
        for x in range(M):
            kill += arr[y+i][x+j]
    return kill

T = int(input())
for idx in range(T):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    max_kill = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            if kill_fly() > max_kill:
                max_kill = kill_fly()

    print(f'#{idx+1} {max_kill}')
