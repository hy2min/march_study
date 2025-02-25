n = int(input())
y, x = 5, 5

for _ in range(n) : 
    order = input()
    if order == 'down' :
        y += 1
    elif order == 'up' :
        y -= 1
    elif order == 'left' : 
        x -= 1
    elif order == 'right' : 
        x += 1
    elif order == 'click' : 
        print(f'{y},{x}')