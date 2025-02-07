win=[[3,5,1],[4,2,6]]
people=list(map(int,input().split()))
dat=[0]*10

for i in win:
    for j in i :
        dat[j] += 1

for i in people:
    if dat[i] ==0:
        print(f'{i}번 불불합격')    
        continue
    print(f'{i}번 합격')