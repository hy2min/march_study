arr = [
    ['BHC','BBQ','KFC'],
    ['MC','7AVE','PAPA'],
    ['DHC','OBS','MOMS'],
]
y,x = map(int, input().split())
d_y = [-1,0,1,0]
d_x = [0,-1,0,1]
for i in range(4):
    dy = y + d_y[i]
    dx = x + d_x[i]
    if dy<0 or dx<0 or dy >=3 or dx >= 3:
        continue
    print(arr[dy][dx], end="")