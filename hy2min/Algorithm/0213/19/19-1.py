arr = [
    [3, 5, 4],
    [1, 1, 2],
    [1, 3, 9],
]

y, x = map(int, input().split())
def delta_sum(y,x):
    d_y = [1, -1, 0, 0]
    d_x = [0, 0, 1, -1]
    total = 0
    for i in range(4):
        dy = y + d_y[i]
        dx = x + d_x[i]
        if dy < 0 or dx < 0 or dy >= len(arr) or dx >= len(arr[0]):
            continue
        total += arr[dy][dx]
    return total

result = delta_sum(y, x)
print(result)
