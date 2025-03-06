N = int(input())
arr = list(map(int, input().split()))
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    if a == 1:
        for i in range(b-1, N, b):
            arr[i] = (arr[i]+1)%2
    elif a == 2:
        b -= 1
        arr[b] = (arr[b]+1)%2
        for i in range(1, N):
            if b-i < 0 or b+i >= N:
                break
            if arr[b-i] == arr[b+i]:
                arr[b-i] = (arr[b-i]+1)%2
                arr[b+i] = (arr[b+i]+1)%2
            else:
                break
for i in range(0, len(arr), 20):
    print(*arr[i:i+20])