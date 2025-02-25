map_arr = [
    [3,3,5,3,1],
    [2,2,4,2,6],
    [4,9,2,3,4],
    [1,1,1,1,1],
    [3,3,5,9,2],
]
max_total = float('-inf')
max_y = -1
max_x = -1

def interaction_sum(y,x):
    total = 0
    d_y = [1, 1, -1, -1]
    d_x = [1, -1, 1, -1]
    for i in range(4):
        dy = y + d_y[i]
        dx = x + d_x[i]
        if 0 <= dy < len(map_arr) and 0 <= dx < len(map_arr[0]):
            total += map_arr[dy][dx]

    return total

for i in range(5):
    for j in range(5):
        if max_total < interaction_sum(i,j):
            max_total = interaction_sum(i,j)
            max_y = i
            max_x = j

print(max_y, max_x)
