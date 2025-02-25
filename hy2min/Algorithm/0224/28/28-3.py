arr = [
    [0,1,1,0,0,0,0,1],
    [0,0,0,0,0,0,0,0],
    [0,0,0,1,1,0,1,0],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
]

bro = input()
bro = ord(bro)-65

parent = None

for i in range(8):
    if arr[i][bro] == 1:
        parent = i
        break
if parent is None:
    print('없음')
else:
    for i in range(8):
        if arr[parent][i] == 1 and i != bro:
            print(chr(i+65), end=" ")