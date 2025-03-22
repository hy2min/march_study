# import sys
# sys.stdin = open("input.txt","r")

def babyjin(lst):

    for i in range(10):
        if lst[i] == 3:
            return 1

    for i in range(8):
        if lst[i] > 0 and lst[i+1] > 0 and lst[i+2] > 0:
            return 1

    return 0


T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    player1 = [0] * 10
    player2 = [0] * 10

    for i in range(12):
        if i < 4:
            if i % 2 == 0:
                player1[arr[i]] += 1
            else:
                player2[arr[i]] += 1
        else:
            if i % 2 == 0:
                player1[arr[i]] += 1
                flag = babyjin(player1)
                if flag:
                    print(f"#{tc} 1")
                    break
            else:
                player2[arr[i]] += 1
                flag = babyjin(player2)
                if flag:
                    print(f"#{tc} 2")
                    break
    else:
        print(f"#{tc} 0")