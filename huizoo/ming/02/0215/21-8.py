y, x = 5, 5
N = int(input())
for _ in range(N):
    order = input()
    if order == 'down':
        y += 1
    elif order == 'up':
        y -= 1
    elif order == 'right':
        x += 1
    elif order == 'left':
        y -= 1
    else:
        print(f'{y},{x}')
