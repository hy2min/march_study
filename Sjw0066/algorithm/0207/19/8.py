image=[list(map(int,input().split())) for _ in range(4)]

def rectSum(y,x):
    sum1=0
    for i in range(2):
        for j in range(3):
            ny=y+i
            nx=x+j

            if ny>3 or ny<0 or nx>3 or nx<0:
                continue
            sum1+=image[ny][nx]

    return sum1

max_sum=-21e8
y=0
x=0
for i in range(4):
    for j in range(4):
        sum1=rectSum(i,j)
        if sum1>max_sum:
            max_sum=sum1
            y=i
            x=j

print(f'({y},{x})')   