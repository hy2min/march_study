lst=[[4, 2, 3, 5],
     [1, 1, 2, 3],
     [4, 7, 6, 4]]

target=[[1, 2],
        [7, 6]]

def isPattern(y, x):
    for i in range(2):
        for j in range(2):
            if target[i][j] != lst[i+y][j+x]:
                return 0
    return 1

ret = 0
for i in range(2):
    for j in range(3):
        ret = isPattern(i,j)
        if ret == 1:
            break
    if ret == 1:
        break
if ret == 1:
    print('찾음')
else:
    print('없음')