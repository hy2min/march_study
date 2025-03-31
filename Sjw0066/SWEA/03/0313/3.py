T=int(input())

def baby(lst1):

    for i in range(10):
        if lst1[i]>=3:
            return True

    for i in range(8):
        if lst1[i]>0 and lst1[i+1]>0 and lst1[i+2]>0:
            return True

    return False

for tc in range(1,T+1):
    lst=list(map(int,input().split()))
    player1=[0]*10
    player2=[0]*10

    for i in range(12):
        if i%2==0:
            player1[lst[i]]+=1
        else:
            player2[lst[i]]+=1

        flag1=baby(player1)
        flag2=baby(player2)

        if flag1:
            print(f'#{tc} 1')
            break
        if flag2:
            print(f'#{tc} 2')
            break
    if not flag1 and not flag2:
        print(f'#{tc} 0')

