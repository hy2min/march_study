T = int(input())

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    lst = [0] * (N + 1)
    for i in range(M):
        node_num, node_val = map(int, input().split())
        lst[node_num] = node_val

    for i in range(N, -1, -1):
        index = i + 1

        if 2 * index > N:
            continue

        if 2 * index + 1 > N:
            lst[index] = lst[2 * index]
            continue

        lst[index] = lst[2 * index] + lst[2 * index + 1]

    print(f'#{tc} {lst[L]}')