t = int(input())
for tc in range(1, t+1):
    N = int(input())
    arr = list(map(int, input().split()))
    Min = arr[0]
    Max = arr[0]
    for i in range(1, N):
        if arr[i] > Max:
            Max = arr[i]
        if arr[i] < Min:
            Min = arr[i]
    print(f'#{tc} {Max-Min}')