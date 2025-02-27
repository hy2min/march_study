target=input()
cnt=0
path=['']*3
name=['A','B','C','D']
def abc(level):
    global cnt

    if level==3:
        cnt+=1
        if ''.join(path) == target:
            print(f'{cnt}번째')
        return

    for i in range(4):
        path[level] = name[i]
        abc(level+1)
        path[level] = ''

abc(0)