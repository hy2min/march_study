vect=['B','T','K','I','G','Z']

target=list(map(str,input().split()))


cnt=0
for i in range(len(target)):
    if target[i] in vect :
        cnt += 1

print(cnt)