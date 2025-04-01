arr =  [[3, 5, 4, 2, 5],
        [3, 3, 3, 2, 1],
        [3, 2, 6, 7, 8], 
        [9, 1, 1, 3, 2]]

y, x = map(int, input().split())

def Find_sum(q, w):
    Sum = 0
    for i in range(y):
        for j in range(x):
            Sum += arr[q + i][w + j]
    return Sum


Max = -1e8
Max_y = 0
Max_x = 0
for i in range(5 - y):
    for j in range(6 - x):
        result = Find_sum(i, j)
        if Max < result:
            Max = result
            Max_y = i
            Max_x = j
print(f'({Max_y},{Max_x})')
