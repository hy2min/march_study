name = ['Amy', 'Bob', 'Chloe', 'Diane', 'Edger']
arr = [
    [0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
max_like = 0
max_idx = -1
like = [0] * 5
for i in range(5):
    like = 0
    for j in range(5):
        if arr[j][i] == 1:
            like += 1
    if max_like < like:
        max_like = like
        max_idx = i

print(name[max_idx])
