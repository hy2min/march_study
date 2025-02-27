arr=[list(input()) for _ in range(3)]

answer=[]
for i in range(3):
    answer.append(arr[i][len(arr[i])-1:])

for i in answer:
    for j in i :
        print(j,end="")