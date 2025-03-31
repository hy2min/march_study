lst=list(map(int,input().split()))

result=[0]*12
result[2]=lst[2]
result[3]=lst[3]

for i in range(4,12):
    ret1=result[i-2]+lst[i]
    ret2 = result[i // 2] + lst[i]
    ret3=result[i-3]+lst[i]


    result[i] = ret1
    if i%2==0:
        if result[i]<ret2:
            result[i] = ret2
    if i>4:
        if result[i]<ret3:
            result[i]=ret3

Max=-21e8
for i in range(6,12):
    Max=max(result[i],Max)

print(Max)



