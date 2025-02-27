floor=1

for i in range(5):
    up_down=input()
    if up_down == 'up':
        floor+=1
    if up_down == 'down':
        floor-=1

if floor<=0:
    floor-=1
    print(f'B{abs(floor)}')
else:
    print(abs(floor))
