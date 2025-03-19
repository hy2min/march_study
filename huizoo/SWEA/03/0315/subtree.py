def search(x):
    if x == 0:
        return 0
    return 1 + search(left[x]) + search(right[x])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = tuple(map(int, input().split()))
    left = [0]*(E+2)
    right = [0]*(E+2)
    for i in range(E):
        p, c = arr[2*i], arr[2*i+1]
        if not left[p]:
            left[p] = c
        else:
            right[p] = c
    print(f'#{tc} {search(N)}')
