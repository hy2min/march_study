# import sys
# sys.stdin = open("input.txt","r")

T = 10
for tc in range(1,T+1):
    M,A = input().split()
    n = int(M)
    lst = list(map(int,A))
    while 1:
        left,right = -1,-1   # 좌우 확인
        N = len(lst)
        if N == 1:
            break
        for i in range(N-1):
            if lst[i] == lst[i+1]:
                left,right = i,i+1
                break
        if left == -1:
            break
        else:
            tmp = 0
            while 1:
                if left-tmp >= 0 and right+tmp < N and lst[left-tmp] == lst[right+tmp]:
                    tmp += 1
                else:
                    break
            del lst[left-tmp+1:right+tmp]

    print(f"#{tc}",end=' ')
    for i in lst:
        print(i,end='')
    print()
