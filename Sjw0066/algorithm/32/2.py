N=int(input())
arr=[]
arr2=[0]
for i in range(N):
    a,b=input().split()
    for j in range(len(arr2)):
        if int(b)>=arr2[j]:
            arr.insert(j,a)
            arr2.insert(j,int(b))
            break
    for i in range(len(arr)):
        if i>2:break
        print(arr[i],end=" ")
    print()