def abc(level):
    global cnt
    cnt += 1
    if level==l:
        return

    for i in range(branch):
        abc(level+1)

branch,l=map(int,input().split())
cnt=0
abc(0)

print(cnt)