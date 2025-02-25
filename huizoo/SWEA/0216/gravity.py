t = int(input())
for tc in range(1, t+1):
    N = int(input())
    arr = list(map(int, input().split()))
    Max = 0
    for i in range(N-1):
        cnt = 0
        for j in range(i+1, N):
            if arr[i] > arr[j]:
                cnt += 1
        if Max < cnt:
            Max = cnt
    print(f'#{tc} {Max}')
