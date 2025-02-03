arr=['A','B','K','T'],['K','F','C','F'],['B','B','Q','Q'],['T','P','Z','F']
a,b=map(str,input().split())
count=0
for i in arr:
    for j in i:
        if j==a:
            count+=1
        if j==b:
            count+=1
print(count)