lst=[list(map(int,input())) for _ in range(3)]

lst.sort(key=lambda x:len(x),reverse=True)
answer=[]
if len(lst[0]) == len(lst[1]):
    for i in range(len(lst[0])):
        if lst[0][i] > lst[1][i]:
            answer=lst[0]
            break
        if lst[0][i]<lst[1][i]:
            answer=lst[1]
            break

for i in answer:
    print(i,end="")