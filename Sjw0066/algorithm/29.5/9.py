str1=input()
str2=input()

arr=[[0]*(len(str2)+1) for _ in range(len(str1)+1)]

for i in range(1,len(arr)):
    for j in range(1,len(arr[i])):
        if str1[i-1] == str2[j-1]:
            arr[i][j] = arr[i-1][j-1]+1

st=0
ed=0
Max=-21e8
for i in range(1,len(arr)):
    for j in range(1,len(arr[i])):
        if Max<arr[i][j]:
            Max=arr[i][j]
            ed=j
            st=j-Max

for i in range(st,ed):
    print(str2[i],end="")

