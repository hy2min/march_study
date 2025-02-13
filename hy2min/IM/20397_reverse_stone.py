def stone(i, j):
    for x in range(1,j+1):
        if i-x >= 0 and i + x < N:
            if state[i-x] == state[i+x] == 1:
                state[i-x] = state[i+x] = 0
            elif state[i-x] == state[i+x] == 0:
                state[i-x] = state[i+x] = 1
    return state


T = int(input())
for idx in range(T):
    N, M = map(int, input().split())
    state = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())
        i -= 1
        stone(i, j)

    print(f'#{idx+1} {" ".join(map(str,state))}')
