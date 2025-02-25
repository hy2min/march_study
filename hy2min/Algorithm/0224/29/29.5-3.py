arr = [list(map(int, input().split())) for _ in range(3)]

for i in range(3):
    if arr[i] == [arr[i][0]] * 3:
        print(arr[i][0])
    else:
        print('x')