mapp = [
    [3,5,1],
    [3,8,1],
    [1,1,5],
]
bit = [list(map(int, input().split())) for _ in range(2)]
Max = 0
y, x = 0, 0
for i in range(2):
    for j in range(2):
        Sum = 0
        for k in range(2):
            for l in range(2):
                if bit[k][l]:
                    Sum += mapp[i+k][j+l]
        if Max<Sum:
            Max = Sum
            y, x = i, j
print(f'({y},{x})')