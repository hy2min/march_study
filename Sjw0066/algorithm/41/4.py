n=int(input())
cnt=0
def abc(level,Sum):
    global cnt

    if Sum>7:
        return

    if level == n:
        if Sum==7:
            cnt+=1
        return

    for i in range(10):
        abc(level+1,Sum+i)

abc(0,0)
print(cnt)