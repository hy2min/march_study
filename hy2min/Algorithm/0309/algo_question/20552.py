t = int(input())
for tc in range(1, t+1):
    cnt = 0
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    arr.sort()
    for i in range(n):
        for j in range(i+1, n):
            if arr[i][1] > arr[j][1]:
                cnt += 1
    print(f'#{tc} {cnt}')