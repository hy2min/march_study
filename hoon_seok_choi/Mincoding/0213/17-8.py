arr = ['B','T','K','I','G','Z']

target = list(map(str,input().split()))

cnt =0

for i in target :
    if i in arr : 
        cnt +=1

print(cnt)
