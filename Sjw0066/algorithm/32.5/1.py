arr=['ABCD','ABCE','AGEH','EIEI','FEQE','ABAD']

str1=input()
ans=[]
cnt=0
for i in range(len(str1)):
    if str1[i] =='?':
        continue
    ans.append(i)


for i in arr:
    flag = 0
    for j in ans:
        if i[j] != str1[j]:
            flag=1
    if not flag:
        cnt+=1

print(cnt)