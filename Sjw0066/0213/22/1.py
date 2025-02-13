name=['A','B','C']
path=[0]*2

def abc(level):

    if level==2:
        print(path[0],end="")
        print(path[1],end="")
        print()
        return

    for i in range(3):
        path[level]=name[i]
        abc(level+1)
        path[level]=0
abc(0)