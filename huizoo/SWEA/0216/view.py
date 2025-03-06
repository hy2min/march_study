for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(2, N-2):
        if arr[i] == max(arr[i-2:i+3]):
            Min = 21e8
            for j in range(i-2, i+3):
                if j != i and Min > arr[i] - arr[j]:
                    Min = arr[i] - arr[j]
            cnt += Min

    print(f'#{tc} {cnt}')