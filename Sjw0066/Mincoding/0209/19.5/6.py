map=[['A','B','G','K'],['T','T','A','B'],['A','C','C','D']]

pattern=[list(input()) for _ in range(2)]

def check_pattern(y,x):
    for i in range(2):
        for j in range(2):
            flag=0
            ny=y+i
            nx=x+j
            if ny>2 or ny<0 or nx>3 or nx<0:
                continue
            if map[ny][nx]==pattern[i][j]:
                flag=1

    return flag
cnt=0

for i in range(3):
    for j in range(4):
        flag=check_pattern(i,j)
        if flag:
            cnt+=1

if cnt:
    print(f'발견({cnt}개)')
else:
    print('미발견')
