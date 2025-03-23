arr = [
    [[2, 4], [1, 5]],
    [[2, 3], [3, 6]],
    [[7, 3], [1, 5]],
]

n = int(input())

max_arr = -21e8
min_arr = 21e8

for i in range(2) : 
    temp_max = max(arr[n][i])
    temp_min = min(arr[n][i])
    if temp_max > max_arr : 
        max_arr = temp_max
    if temp_min < min_arr : 
        min_arr = temp_min

print(f'MAX={max_arr}')
print(f'MIN={min_arr}')