maping = [[3, 55, 42], [-5, -9, -10]]
pix = [list(map(int, input().split())) for _ in range(2)]

def isExist(num):
    for i in range(2):
        for j in range(3):
            if maping[i][j] == num:
                return 'Y'
    return 'N'


for i in range(2):
    for j in range(2):
        print(isExist(pix[i][j]), end = " ")
    print()