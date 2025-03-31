arr = [[['A', 'T', 'B'], ['C', 'C', 'B']], [['A', 'A', 'A'], ['B', 'B', 'C']]]
char = input()
Flag = 0
def find_char(lev):
    global Flag
    if lev == 2:
        return

    for i in range(2):
        for j in range(3):
            if arr[lev][i][j] == char:
                Flag = 1
                return
            else: find_char(lev + 1)


find_char(0)
if Flag:
    print('발견')
else: print('미발견')