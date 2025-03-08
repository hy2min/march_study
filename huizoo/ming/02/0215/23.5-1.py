arr = [3,5,1,9,7]
for _ in range(4):
    order = input()
    if order == 'R':
        arr = [arr[-1]] + arr[:4]
    elif order == 'L':
        arr = arr[1:5] + [arr[0]]

print(*arr)