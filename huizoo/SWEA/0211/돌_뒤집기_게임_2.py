def change(i, j):
    for k in range(1, j+1) :
        left, right = i-k, i+k
        if 0 <= left < N and 0 <= right < N:
            if rock[left] == rock[right]:
                rock[left] = (rock[left] + 1) % 2
                rock[right] = (rock[right] + 1) % 2
        else:
            return
    return

t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    rock = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())
        i -= 1
        change(i, j)

    print(f'#{tc}', *rock)