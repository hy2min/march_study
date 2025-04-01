arr = [list(map(str, input())) for _ in range(3)]

Max_str = -1e8
Max_in = -1e8
for i in range(3):
    if len(arr[i]) > Max_str:
        Max_str = len(arr[i])
        Max_in = i

arr[Max_in], arr[0] = arr[0], arr[Max_in]

for i in range(3):
    print(*arr[i], sep = '')