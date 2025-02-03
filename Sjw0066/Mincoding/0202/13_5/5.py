arr=[[4,5,7,1,3,2],['D','F','Q','W','G','Z']]

x=int(input())
index=0

for i in range(len(arr[0])):
    if arr[0][i]==x:
        index=i

print(arr[1][index])