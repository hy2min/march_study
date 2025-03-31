arr=[
    [3,5,4,2,5],
    [3,3,3,2,1],
    [3,2,6,7,8],
    [9,1,1,3,2],
]

def Sum_squar(y,x):
    sum_sq=0
    for i in range(a):
        for j in range(b):
            ny=y+i
            nx=x+j
            if ny<0 or ny>3 or nx<0 or nx>4:
                continue
            sum_sq+=arr[ny][nx]

    return sum_sq

a,b= map(int,input().split())

sum1=0
max_sum=-21e8
y_index=0
x_index=0
for i in range(4):
    for j in range(5):
        sum1= Sum_squar(i,j)
        if sum1>max_sum:
            max_sum=sum1
            y_index=i
            x_index=j

print(f'({y_index},{x_index})')