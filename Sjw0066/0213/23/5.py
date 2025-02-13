name=['E','W','A','B','C']
n=4
path=[0]*4
used=[0]*5

no_name=input()
for i in range(len(name)):
    if name[i] == no_name:
        no_index=i

def abc(level):


    if level == n :
        for i in range(4):
            print(path[i],end="")
        print()
        return

    for i in range(5):
        if used[i] == 1 or i == no_index:
            continue
        used[i] = 1
        path[level] = name[i]
        abc(level+1)
        path[level]=0
        used[i] = 0

abc(0)
