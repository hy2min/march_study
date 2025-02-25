arr = [list(input()) for _ in range(4)]

def find_idx(s):
    for i in range(4):
        for j in range(3):
            if arr[i][j] == s:
                y_idx = i
                x_idx = j
    return y_idx, x_idx
ret_y = abs(find_idx("A")[0] - find_idx("B")[0])
ret_x = abs(find_idx("A")[1] - find_idx("B")[1])

print(ret_y + ret_x)
