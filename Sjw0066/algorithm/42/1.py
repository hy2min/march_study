name=list(input())
path=[0]*3


def abc(level,st):

    if level==3:
        print(*path,sep="")
        return

    for i in range(st,len(name)):
        path[level] = name[i]
        abc(level+1,i)

abc(0,0)