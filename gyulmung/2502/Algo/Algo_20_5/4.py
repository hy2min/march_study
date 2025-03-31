bit1 = [list(map(int, input().split())) for _ in range(5)]
bit2 = [list(map(int, input().split())) for _ in range(4)]

Flag = False
for i in range(4):
    for j in range(4):
        if bit1[i][j] == 1 and bit2[i][j] == 1:
            Flag = True

if Flag:
    print('걸리다')
else:
    print('걸리지않는다')