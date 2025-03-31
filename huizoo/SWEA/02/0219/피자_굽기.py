t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    queue = []
    for i, x in enumerate(arr[:N]):
        queue.append([x, i])
    nxt = N
    while len(queue) > 1:
        x, i = queue.pop(0)
        x //= 2

        if x > 0:
            queue.append([x, i])
        else:
            if nxt < M:
                queue.append([arr[nxt], nxt])
                nxt += 1
    print(f'#{tc} {queue[0][1]+1}')