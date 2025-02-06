DAT=[0]*65536
data=[65000,35,42,70],[70,35,65000,1300],[65000,30000,38,42]
for i in data:
    for j in i:
        DAT[j]+=1
'''       
count=max(DAT)
for i in range(1,65536):
    if count==DAT[i]:
        print(i)
''' 
count=0
id=0
for i in range(1,65536):
    if count<DAT[i]:
        count=DAT[i]
        id=i
print(id)