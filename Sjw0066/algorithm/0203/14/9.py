arr1=[10,50,40,20,30,40]

arr2=list(map(int,input().split()))

answer=[]

for i in arr2:
    cnt=0
    for j in arr1:
        if i<j :
           cnt+=1
    answer.append(cnt) 

for i in range(6):
    print(f'{arr2[i]}={answer[i]}개')