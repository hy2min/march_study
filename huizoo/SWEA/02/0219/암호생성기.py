from collections import deque
for tc in range(1, 11):
    n = input()
    arr = list(map(int, input().split()))
    q = deque(arr)
    stop = 0
    while stop == 0:
        for i in range(1, 6):
            a = q.popleft() - i
            if a <= 0:
                a = 0
            q.append(a)
            if not a:
                stop = 1
                break

    print(f'#{tc}', *q)