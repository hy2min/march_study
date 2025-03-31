for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(N):
        arr[arr.index(max(arr))] -= 1
        arr[arr.index(min(arr))] += 1
    print(f'#{tc} {max(arr) - min(arr)}')