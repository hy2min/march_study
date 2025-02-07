MAP= [
    [3, 3, 5, 3, 1],
    [2, 2, 4, 2, 6],
    [4, 9, 2, 3, 4],
    [1, 1, 1, 1, 1],
    [3, 3, 5, 9, 2]
]

direct_y=[-1,1,1,-1]
direct_x=[-1,-1,1,1]

def Sum(y,x):
    sum1=0
    for i in range(len(direct_x)):
        dy=y+direct_y[i]
        dx=x+direct_x[i]
        if dy<0 or dy>4 or dx<0 or dx>4:
            continue
        sum1 += MAP[dy][dx]
    return sum1
max_sum=-21e8

for i in range(len(MAP)):
    for j in range(len(MAP[i])):
        sum1=Sum(i,j)

        if max_sum<sum1:
            max_sum=sum1
            y=i
            x=j

print(y,x)
