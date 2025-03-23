T = int(input())
for tc in range(1, T+1):
    n, *arr = list(map(int, input().split()))
    n -= 1
    now = 0
    cnt = 0
    drive = arr[0]
    flag = 0
    while 1:
        Max = 0
        cnt += 1
        for i in range(now+1, now+drive+1):
            if Max < i+arr[i]:
                Max = i+arr[i]
                if Max >= n:
                    flag = 1
                    break
                now = i
                drive = arr[i]
        if flag:
            break

    print(f'#{tc} {cnt}')