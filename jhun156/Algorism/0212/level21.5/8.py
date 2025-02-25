# import sys
# sys.stdin = open("input.txt","r")

arr = [
    ['_','_','_'],
    ['_','_','_'],
    ['A','T','K'],
    ['_','_','_'],
    ['_','_','_'],
]
# n = 7
make = [list(input().split()) for _ in range(7)]

Ay,Ax,Ty,Tx,Ky,Kx = 2,0,2,1,2,2

def move(CH,STR):
    global arr
    global Ay,Ax,Ty,Tx,Ky,Kx
    if CH == 'A':
        if STR == 'UP':
            arr[Ay][Ax],arr[Ay-1][Ax] = arr[Ay-1][Ax],arr[Ay][Ax]
            Ay -= 1
        elif STR == 'DOWN':
            arr[Ay][Ax], arr[Ay+1][Ax] = arr[Ay+1][Ax], arr[Ay][Ax]
            Ay += 1
        elif STR == 'RIGHT':
            arr[Ay][Ax+1], arr[Ay][Ax] = arr[Ay][Ax], arr[Ay][Ax+1]
            Ax += 1
        else:
            arr[Ay][Ax-1], arr[Ay][Ax] = arr[Ay][Ax], arr[Ay][Ax-1]
            Ax -= 1
    elif CH == 'T':
        if STR == 'UP':
            arr[Ty][Tx],arr[Ty-1][Tx] = arr[Ty-1][Tx],arr[Ty][Tx]
            Ty -= 1
        elif STR == 'DOWN':
            arr[Ty][Tx], arr[Ty+1][Tx] = arr[Ty+1][Tx], arr[Ty][Tx]
            Ty += 1
        elif STR == 'RIGHT':
            arr[Ty][Tx+1], arr[Ty][Tx] = arr[Ty][Tx], arr[Ty][Tx+1]
            Tx += 1
        else:
            arr[Ty][Tx-1], arr[Ty][Tx] = arr[Ty][Tx], arr[Ty][Tx-1]
            Tx -= 1
    else:
        if STR == 'UP':
            arr[Ky][Kx],arr[Ky-1][Kx] = arr[Ky-1][Kx],arr[Ky][Kx]
            Ky -= 1
        elif STR == 'DOWN':
            arr[Ky][Kx], arr[Ky+1][Kx] = arr[Ky+1][Kx], arr[Ky][Kx]
            Ky += 1
        elif STR == 'RIGHT':
            arr[Ky][Kx+1], arr[Ky][Kx] = arr[Ky][Kx], arr[Ky][Kx+1]
            Kx += 1
        else:
            arr[Ky][Kx-1], arr[Ky][Kx] = arr[Ky][Kx], arr[Ky][Kx-1]
            Kx -= 1

for i in range(7):
    move(make[i][0],make[i][1])

for i in range(5):
    for j in range(3):
        print(arr[i][j],end='')
    print()