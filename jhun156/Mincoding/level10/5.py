a = int(input())
arr = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
]

num = 9

if a % 5 == 1:
    for i in range(3):
        for j in range(3):
            arr[j][i] = num
            num -= 1
elif a % 5 == 2:
    for i in range(3):
        for j in range(3):
            arr[i][2-j] = num
            num -= 1
else:
    for i in range(3):
        for j in range(3):
            arr[j][i] = num +1
            num += 1

for i in range(3):
    for j in range(3):
        print(arr[i][j],end= ' ')
    print()