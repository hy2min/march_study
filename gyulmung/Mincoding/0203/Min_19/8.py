lst = [list(map(int, input().split())) for _ in range(4)]

def rectSum(y, x):
    Sum = 0
    for i in range(2):
        for j in range(3):
            Sum += lst[y + i][x + j]
    return Sum

Max = -1e8

for  i in range(3):
    for j in range(2):
        Total_sum = rectSum(i, j)
        if Max < Total_sum:
            Max = Total_sum
            y, x = i, j

print(f'({y},{x})')