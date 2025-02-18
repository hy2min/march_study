T= int(input())

def dfs(level,Sum):
    global arr,Max
    backup=arr[:]

    if level==N:


        return

    for i in range(len(arr)):
            score=
            dfs(level+1,Sum+score)
            arr=backup[:]

for tc in range(1,T+1):
    N=int(input())
    arr=list(map(int,input().split()))
    Max=-21e8



dfs(0)
print(Max)