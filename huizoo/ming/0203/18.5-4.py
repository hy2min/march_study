up = list(map(int, input().split()))
down = list(map(int, input().split()))
dat = [0]*5
for i in range(5) : 
    if up[i] : 
        dat[i] += 1
    if down[i] : 
        dat[i] += 1
print(f'{dat.count(2)}개')