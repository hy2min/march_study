freinds = ['E','W','A','B','C']
OD = input()
freinds.remove(OD)
path = [0]*4
used = [0]*4

def select(num):

    if num == 4:
        for i in range(4):
            print(path[i],end='')
        print()

    for i in range(4):
        if used[i] == 1: continue
        path[num] = freinds[i]
        used[i] = 1
        select(num+1)
        used[i] = 0

select(0)
