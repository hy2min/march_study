def abc(num,ed,ite):

    global cnt
    cnt += 1

    if num == ed:
        return

    for i in range(ite):
        abc(num+1,ed,ite)

cnt = 0
branch,level = map(int,input().split())
abc(0,level,branch)
print(cnt)