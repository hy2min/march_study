arr = [3, 7, 4, 1, 2, 6]

univer = [list(map(int, input().split())) for _ in range(2)]

def Find_num(num):
    for i in arr:
        if i == num:
            return 'OK'
    return 'NO'

for i in range(2):
    for j in range(2):
        print(Find_num(univer[i][j]), end = ' ')
    print()