l=int(input())
d=int(input())

def abc(level):

    if level==l:
        return

    for i in range(d):
        abc(level+1)

abc(0)
