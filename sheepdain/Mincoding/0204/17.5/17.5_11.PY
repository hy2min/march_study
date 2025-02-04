data=[3,5,4,2]
beat=list(map(int,input().split()))
SUM=0
for i in range(4):
    if beat[i]==1:
        SUM+=data[i]
print(SUM)
        