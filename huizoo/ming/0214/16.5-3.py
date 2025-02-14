def min_arr(lst):
    ret = 21e8
    y, x = 0, 0
    for i in range(2):
        for j in range(3):
            if lst[i][j] < ret:
                ret = lst[i][j]
                y, x = i, j
    return y, x

def max_arr(lst):
    ret = -21e8
    y, x = 0, 0
    for i in range(2):
        for j in range(3):
            if lst[i][j] > ret:
                ret = lst[i][j]
                y, x = i, j
    return y, x


arr = list(map(int, input().split()))
nums = [arr[:3], arr[3:]]
y1, x1 = max_arr(nums)
y2, x2 = min_arr(nums)
print(f'({y1},{x1})')
print(f'({y2},{x2})')