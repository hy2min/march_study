t = int(input())
for tc in range(1, t+1):
    n, m, l = map(int,input().split())
    arr = [0] * (n+1)
    for _ in range(m):
        node, num = map(int, input().split())
        arr[node] = num
    if n % 2 == 0:
        arr[n//2] = arr[n]    
        for i in range((n//2)-1, 0, -1):
            arr[i] = arr[2*i] + arr[2*i + 1]
    else:
        for i in range(n//2, 0, -1):
            arr[i] = arr[2*i] + arr[2*i + 1]
    print(f'#{tc} {arr[l]}')