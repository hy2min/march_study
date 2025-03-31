# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    special = []
    tmp = 0
    while tmp < 5:
        special.append(max(lst))
        special.append(min(lst))
        lst.remove(max(lst))
        lst.remove(min(lst))
        tmp += 1

    print(f"#{tc} ", end ='')
    for i in range(10):
        print(special[i],end =' ')
    print()