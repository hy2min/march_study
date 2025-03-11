t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    Max = 0
    for i in range(n-1):
        cnt = 0
        now = arr[i]
        for j in range(i, n):
            if now < arr[j]:
                cnt += 1
                now = arr[j]
        Max = max(cnt, Max)
    print(f'#{tc} {Max}')
