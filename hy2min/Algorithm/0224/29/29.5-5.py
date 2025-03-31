arr = [list(map(int, input().split())) for _ in range(4)]

min_i = 21e8
min_j = 21e8

max_i = -21e8
max_j = -21e8


for i in range(4):
    for j in range(5):
        if arr[i][j] == 1 and min_i> i:
            min_i = i
        if arr[i][j] == 1 and min_j > j:
            min_j = j

for i in range(4):
    for j in range(5):
        if arr[i][j] == 1 and max_i < i:
            max_i = i
        if arr[i][j] == 1 and max_j < j:
            max_j = j

print(f'({min_i},{min_j})')
print(f'({max_i},{max_j})')

