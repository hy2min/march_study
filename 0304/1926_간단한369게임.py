n = int(input())

arr = list(range(1, n+1))
for i in arr:
    cnt= 0
    for j in str(i):
        if j =='3':
            cnt +=1 
        if j =='6':
            cnt +=1 
        if j =='9':
            cnt +=1 
    if cnt > 0:
        print('-'*cnt, end=" ")
    else:
        print(i, end=" ")