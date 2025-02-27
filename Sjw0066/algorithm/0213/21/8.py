def mouse(level,y,x):
    if level == n:
        return

    order= input()

    if order=='up':
        y-=1

    if order=='down':
        y+=1

    if order=='left':
        x-=1

    if order=='right':
        x+=1

    if order=='click':
        print(f'{y},{x}')

    mouse(level+1,y,x)



n=int(input())
mouse(0,5,5)

