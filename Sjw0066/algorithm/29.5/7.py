a,b=map(int,input().split())

arr=[[0]*5 for _ in range(b+1)]

def abc(level,index,life):

    if index>4 or life==0:
        return

    arr[level][index]=life
    abc(level+1,index+1,life-1)

abc(0,a,b)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 0 :
            print('_',end="")
        else:
            print(arr[i][j],end="")
    print()