import sys
sys.stdin = open("input.txt","r")

T = 10
for tc in range(1,T+1):
    n,A = map(int,input().split())
    a = str(A)
    lst = list(map(int,a))
    sted = []
    for i in range(n-1):
        row = []
        if lst[i] == lst[i+1]:
            row.append(i)
            row.append(i+1)
            sted.append(row)

    m = len(sted)
    tmp_lst = []
    for i in range(m):
        tmp = 0
        while 1:
            if lst[sted[i][0]-tmp] == lst[sted[i][1]+tmp]:
                tmp += 1
            else:
                break
        tmp_lst.append(tmp)

    for i in range(m):
        del lst[sted[i][0]-tmp_lst[i]+1:sted[i][1]+tmp_lst[i]]
    print(*lst)