def abc(num,ed):

    print(num,end='')
    if num == ed:
        return

    for i in range(2):
        abc(num+1,ed)

level = int(input())
abc(0,level)