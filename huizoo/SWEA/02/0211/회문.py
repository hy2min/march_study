def found(lst):
    for i in range(N):
        for j in range(N-M+1):
            if lst[i][j:j+M] == lst[i][j:j+M][::-1]:
                return lst[i][j:j+M]
    return []

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    arr2 = list(zip(*arr))
    ret = max(found(arr), found(arr2), key=len)
    print(f'#{tc} {"".join(ret)}')