arr = [
    [3,5,4,2,2,3],
    [1,3,3,3,4,2],
    [5,4,4,2,3,5],
]
price = 'TPGKC'

idx_y, idx_x = input().split()
idx_y = ord(idx_y) - 65
idx_x = int(idx_x) -1


n = arr[idx_y][idx_x]
print(price[n-1])

