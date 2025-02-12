def abc(num,ed,ite):

    if num == level:
        return

    for i in range(branch):
        abc(num+1,ed,ite)

level = int(input())
branch = int(input())
abc(0,level,branch)