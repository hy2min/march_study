T = int(input())


def abc(now):
    global cnt

    if c1[now] == []:
        return

    for i in c1[now]:
        cnt += 1
        abc(i)


for tc in range(1, T + 1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    c1 = [[] for _ in range(max(lst) + 1)]

    for i in range(0, E * 2, 2):
        c1[lst[i]].append(lst[i + 1])

    cnt = 1
    abc(N)
    print(f'#{tc} {cnt}')