nums = list(map(int, input().split()))
arr = [nums[:3], nums[3:]]
def max_n(arr):
    max_value = -2e18
    max_idx = (0, 0)

    for i in range(2):
        for j in range(3):
            if arr[i][j] > max_value:
                max_value = arr[i][j]
                max_idx = (i, j)
    return max_idx

def min_n(arr):
    min_value = 2e18
    min_idx = (0, 0)

    for i in range(2):
        for j in range(3):
            if arr[i][j] < min_value:
                min_value = arr[i][j]
                min_idx = (i, j)
    return min_idx

print(f'({max_n(arr)[0]},{max_n(arr)[1]})')
print(f'({min_n(arr)[0]},{min_n(arr)[1]})')
