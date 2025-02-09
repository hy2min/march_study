arr2=[[0]*4 for _ in range(4)]
lst1=list(map(int,input().split()))
lst2=[]

val=1
for i in range(4):
    for j in range(4):
        arr2[i][j] = val
        val+=1

val2=1
for i in range(4):
    for j in range(4):
        flag=0
        for k in range(4):
            if arr2[i][j] == lst1[k]:
                arr2[i][j] = val2
                val2+=1
                flag=1
        if flag==0:
            arr2[i][j] = 0     


for i in range(4):
    for j in range(4):
        print(arr2[i][j],end=" ")
    print()