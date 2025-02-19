arr = [
    [3,5,1],
    [3,8,1],
    [1,1,5],
]
bitarray = [list(map(int, input().split())) for _ in range(2)]

def bit_sum(y,x):
    bitsum = 0
    for i in range(2):
        for j in range(2):
            if bitarray[i][j] == 1:
                bitsum += arr[y+i][x+j]
    return bitsum

max_bitsum = -21e8
y_idx, x_idx = -1, -1
for y in range(2):
    for x in range(2):
        if bit_sum(y,x) > max_bitsum:
            max_bitsum = bit_sum(y,x)
            y_idx, x_idx = y, x

print(f'({y_idx},{x_idx})')