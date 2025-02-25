N,K = map(int,input().split())

students=[list(map(int,input().split())) for _ in range(N)]

dat_man=[0]*7
dat_woman=[0]*7

cnt=0
for i in students:
    if i[0] == 0:
        dat_woman[i[1]] +=1
    else:
        dat_man[i[1]] += 1

for i in dat_man:
    if i :
        cnt += 1
    if i>K:
        cnt+=(i-1)//K
for i in dat_woman:
    if i :
        cnt += 1
    if i>K:
        cnt+=(i-1)//K
print(cnt)

