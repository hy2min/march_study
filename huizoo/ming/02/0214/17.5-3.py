def abc(n):
    if n == 99:
        return 1
    for m in road[n]:
        if not visited[m]:
            visited[m] = 1
            ret = abc(m)
            visited[m] = 0
        if ret:
            return 1
    return 0

for tc in range(1, 11):
    t, N = map(int, input().split())
    arr = list(map(int, input().split()))
    road = [[] for _ in range(100)]
    visited=[0]*100
    for i in range(0, 2*N, 2):
        road[arr[i]].append(arr[i+1])
    ans = abc(0)
    print(f'#{tc} {ans}')