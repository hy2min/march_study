arr = [
    [3, 1, 9],
    [7, 2, 1],
    [1, 0, 8],
]
masking = []
for i in range(3):
    masking.append(list(map(int, input().split())))

flag = False
for i in range(3):
    for j in range(3):
        if masking[i][j] == 1:
            if 3<= arr[i][j] <= 5:
                print("발견")
                flag = True
                break
            if flag:
                break
            
if not flag:
    print("미발견")
