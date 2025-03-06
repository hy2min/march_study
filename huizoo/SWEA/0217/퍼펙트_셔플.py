t = int(input())
for tc in range(1, t+1):
    N = int(input())
    arr = list(input().split())
    arr2 = []
    if N % 2 == 0:
        for i in range(N//2):
            arr2.append(arr[i])
            arr2.append(arr[N//2+i])
    elif N % 2 == 1:
        for i in range(N//2):
            arr2.append(arr[i])
            arr2.append(arr[N//2+i+1])
        arr2.append(arr[N//2])
    print(f'#{tc} {" ".join(arr2)}')