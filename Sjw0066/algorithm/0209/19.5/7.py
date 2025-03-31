map1=[[3,5,1],[3,8,1],[1,1,5]]

bitarray =[list(map(int,input().split())) for _ in range(2)]

def sum_masking(y,x):
    sum1=0
    for i in range(2):
        for j in range(2):
            ny=y+i
            nx=x+j
            if ny>2 or ny<0 or nx>2 or nx<0:
                continue
            sum1 += map1[ny][nx]*bitarray[i][j]
    return sum1 

max_sum=-21e8
for i in range(3):
    for j in range(3):
        sum1=sum_masking(i,j)

        if sum1>max_sum:
            max_sum=sum1
            y=i
            x=j

print(f'({y},{x})')

