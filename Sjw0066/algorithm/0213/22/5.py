n=int(input())
path=[0]*4

def abc(level):

    if level==4:
        for i in range(4):
            print(path[i],end="")
        print()
        return

    for i in range(n):
        path[level] = i+1
        abc(level+1)
        path[level] = 0

abc(0)