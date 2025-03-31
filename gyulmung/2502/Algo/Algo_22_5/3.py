arr= [[[0]*3]*3 for _ in range(3)]
char = input()
def fill(lev, char):
    global arr
    if lev == 3:
        return

    for i in range(3):
        for j in range(3):
            arr[lev][i][j] = char
    fill(lev + 1, chr(ord(char) + 1))

fill(0, char)
for i in arr:
    for j in i:
        print(*j, sep = '')
    print()