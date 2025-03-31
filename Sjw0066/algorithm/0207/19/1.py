arr = [[3, 5, 4], [1, 1, 2], [1, 3, 9]]
y, x = map(int, input().split())

direct_x=[1,0,-1,0]
direct_y=[0,1,0,-1]
sum1=0

for i in range(4):
    dy=y+direct_y[i]
    dx=x+direct_x[i]
    if dx<0 or dx>2 or dy<0 or dy>2:
        continue
    sum1+=arr[dy][dx]
print(sum1)