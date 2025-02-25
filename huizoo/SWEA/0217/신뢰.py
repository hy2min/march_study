t = int(input())
for tc in range(1, t+1):
    N, *arr = list(input().split())
    N = int(N)
    orderO = []
    orderB = []
    order = []
    for i in range(0, 2*N, 2):
        if arr[i] == 'O':
            order.append(arr[i])
            orderO.append(int(arr[i+1]))
        elif arr[i] == 'B':
            order.append(arr[i])
            orderB.append(int(arr[i+1]))
    timeO, timeB = 0, 0
    time = 0
    locO, locB = 1, 1

    while order:
        robot = order.pop(0)
        if robot == 'O':
            button = orderO.pop(0)
            move = abs(button - locO)
            locO = button
            wait = min(0, move-(time-timeO))
            timeO += move + 1 - wait
            time = timeO

        if robot == 'B':
            button = orderB.pop(0)
            move = abs(button - locB)
            locB = button
            wait = min(0, move-(time-timeB))
            timeB += move + 1 - wait
            time = timeB

    print(f'#{tc} {time}')