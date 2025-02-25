arr = [
    [
        ['A','T','B'],
        ['C','C','B'],
    ],
    [
        ['A','A','A'],
        ['B','B','C'],
    ],
]

flag = 0
a = input()
for i in range(2):
    for j in range(2):
        for k in range(3):
            if arr[i][j][k] == a:
                flag = 1
                if flag == 1:
                    break
        if flag == 1:
            break
    if flag == 1:
        break

if flag:
    print("발견")
else:
    print("미발견")