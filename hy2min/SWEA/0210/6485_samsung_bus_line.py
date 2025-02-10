T = int(input())
for idx in range(T):
    N = int(input())
    num_range = []
    for _ in range(N):
        num_range.append(list(map(int, input().split())))
    P = int(input())
    bus_line = []
    for _ in range(P):
        bus_line.append(int(input()))
    cnt_lst = []
    for x in bus_line:
        cnt = 0
        for i in range(N):
            if x in range(num_range[i][0], num_range[i][1]+1):
                cnt += 1
        cnt_lst.append(cnt)
    print(f'#{idx+1} {" ".join(map(str,cnt_lst))}')
