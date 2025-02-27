arr=[5,9,4,6,1,5,8,9]

Offset=0
a,b=map(int,input().split())


for i in range(a,len(arr)):
    if arr[i] == b :
        break
    else:
        Offset+=1

print(Offset)