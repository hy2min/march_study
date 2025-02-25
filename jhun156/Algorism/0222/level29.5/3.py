arr = [list(map(int,input().split())) for _ in range(3)]

for i in range(3):
    if arr[i][0] == arr[i][1] == arr[i][2]:
        print(arr[i][0])
    else:
        print("x")