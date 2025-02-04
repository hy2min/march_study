arr= [[5,1,4,2,6],[3,5,0,0,7],[9,9,8,3,1]]

int1=int(input())

cnt=0

for i in arr:
    for j in i:
        if j > int1:
            cnt+=1

print(f'{cnt}개')