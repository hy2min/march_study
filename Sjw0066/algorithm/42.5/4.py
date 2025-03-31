import copy
N=int(input())
target=list(map(int,input().split()))
Max=-21e8
path=[0]*N
answer=[]

def hit(index,lst):
    Sum=0
    temp=lst[:]
    for i in range(-1,2):
        dx=index+i
        if dx>len(temp)-1 or dx<0:continue
        Sum+=temp[dx]
        lst.remove(temp[dx])
    return lst

def dfs(lst,level):
    global Max,answer

    if lst==[]:
        if Max<sum(path):
            Max=sum(path)
            answer=path[:]
        return

    temp=copy.deepcopy(lst)
    for i in range(len(lst)):
        path[level] = temp[i]
        ret=hit(i,lst)
        dfs(ret,level+1)
        path[level]=0
        lst=copy.deepcopy(temp)

dfs(target,0)
answer.sort()


for i in range(len(answer)):
    if answer[i] != 0:
        print(answer[i],end="")
        if i != len(answer)-1:
            print('+',end="")
print('=',end="")
print(sum(answer))
