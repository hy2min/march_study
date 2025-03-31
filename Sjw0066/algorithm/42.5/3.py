name=['!!','#','$','&']
N=int(input())
lst=list(map(int,input().split()))
cnt=0
def cal(a,b,str1):
    if str1=="!!":
        return (a-b)*(a+b)
    elif str1=="#":
        return max(a,b)
    elif str1=="$":
        return a**2-b**2
    elif str1=='&':
        return (a+b)**2

def dfs(Sum,level):
    global cnt

    if Sum>100:
        return

    if level==N-1:
        if Sum==100:
            cnt+=1
        return

    for i in range(4):
        ret=cal(Sum,lst[level+1],name[i])
        dfs(ret,level+1)


dfs(lst[0],0)
print(cnt)


