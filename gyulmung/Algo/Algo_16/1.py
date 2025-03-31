arr = [list(map(str, input())) for _ in range(3)]

for i in range(3):
    print(arr[i][len(arr[i])-1], end = '')