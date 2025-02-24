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

a = input()
a_index = ord(a) - 65
older = -1
for i in range(8) :  
    if arr[i][a_index] == 1:
        older = i
if older == -1 : 
    print('없음')
else : 
    brother = []
    for j in range(8) : 
        if arr[older][j] == 1 : 
            brother.append(chr(j+65))
    brother.remove(a)
    print(*brother)