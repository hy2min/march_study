arr = [
    ['A', 'T', 'K', 'B'],
    ['C', 'Z', 'F', 'D'],
    ['H', 'G', 'E', 'I'],
]
s, y, x = input().split()

for i, row in enumerate(arr):
    for j, value in enumerate(row):
        if value == s:
            y_idx, x_idx = i, j
            break

result = arr[y_idx + int(y)][x_idx + int(x)]
print(result)