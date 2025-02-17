
for  in range(10):
    idx = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if ladder[i][j] == 1:
