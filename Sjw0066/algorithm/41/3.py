T,n=map(int,input().split())
coin=list(map(int,input().split()))
cnt_coin=[21e8]*(T+1)
Min=21e8
flag=0
def count_coin(Sum,cnt):
    global Min,flag

    if Sum>T:
        return

    if Sum==T:
        if Min>cnt:
            Min=cnt
        flag=1
        return

    if cnt_coin[Sum]<=cnt:
        return

    cnt_coin[Sum]=cnt

    for i in range(len(coin)):
        count_coin(Sum+coin[i],cnt+1)

count_coin(0,0)
if flag:
    print(Min)
else:
    print('impossible')

