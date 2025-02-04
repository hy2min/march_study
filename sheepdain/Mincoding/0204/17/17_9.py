vect=[3,7,4],[2,2,4],[2,2,5]
target=list(map(int,input().split()))
def Count(a):
    count=0
    for i in vect:
        for j in i:
            if j==a:
                count+=1
    return count
x={}
arr=[]
for i in target:
    x[i]=Count(i)
    arr.append(Count(i))
for i in target:
    if x[i]==max(arr):
        print(i)
