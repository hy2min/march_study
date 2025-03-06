def pal_odd(y, x):
    length = 1
    for k in range(1, 50):
        left, right = x-k, x+k+1
        if 0 <= left and right <= 100:
            if arr[y][left:right] == arr[y][left:right][::-1]:
                length += 2
            else:
                return length
        else:
            return length
    return length

def pal_even(y, x):
    length = 2
    for k in range(1, 50) :
        left, right = x-k, x+k+2
        if 0 <= left and right <= 100:
            if arr[y][left:right] == arr[y][left:right][::-1]:
                length += 2
            else:
                return length
        else:
            return length
    return length


for tc in range(10):
    t = int(input())
    arr = [list(input()) for _ in range(100)]
    max_length = 1
    for i in range(100):
        for j in range(99):
            if arr[i][j] == arr[i][j+1]:
                current_length = pal_even(i, j)
                if max_length < current_length:
                    max_length = current_length
            else :
                current_length = pal_odd(i, j)
                if max_length < current_length:
                    max_length = current_length

    arr = list(zip(*arr))
    for i in range(100):
        for j in range(99):
            if arr[i][j] == arr[i][j + 1]:
                current_length = pal_even(i, j)
                if max_length < current_length:
                    max_length = current_length
            else:
                current_length = pal_odd(i, j)
                if max_length < current_length:
                    max_length = current_length

    print(f'#{tc+1} {max_length}')