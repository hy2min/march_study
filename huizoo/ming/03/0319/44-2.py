H, W = map(int, input().split())
lst = [list(input().strip()) for _ in range(H)]

N = int(input())
pattern = [list(input().strip()) for _ in range(N)]


def check(ty, tx):
    for py in range(N):
        for px in range(N):
            if ty + py >= H or tx + px >= W:
                return 0
            if lst[ty + py][tx + px] != pattern[py][px]:
                return 0
    return 1


for y in range(H):
    for x in range(W):
        if check(y, x):
            print(f"{y},{x}")