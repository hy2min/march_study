up=list(map(int,input().split()))
down=list(map(int,input().split()))

cnt=0
for i,j in zip(up,down):
    if i&j :
        cnt +=1

print(f'{cnt}개')