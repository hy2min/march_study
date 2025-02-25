arr = list(map(int, input().split()))

for i in range(4,8):
    print(*arr[:i])