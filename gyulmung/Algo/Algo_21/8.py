N = int(input())
sys = [input() for _ in range(N)]
y, x = 5, 5

def curser(lev):
    global y, x
    if lev == N:
        return
    if sys[lev] == 'up':
        y -= 1
    elif sys[lev] == 'down':
        y += 1
    elif sys[lev] == 'left':
        x -= 1
    elif sys[lev] == 'right':
        x += 1
    elif sys[lev] == 'click':
        print(f'{y},{x}')


    curser(lev + 1)

curser(0)
