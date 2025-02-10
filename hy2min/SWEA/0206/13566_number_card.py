T = int(input())
for idx in range(T):
    N = int(input())
    lst = list(map(int, input()))
    max_cnt = float('-inf')
    max_n = float('-inf')
    for i in sorted(lst, reverse=True):
        cnt = lst.count(i)
        if cnt > max_cnt:
            max_cnt = cnt
            max_n = i
    print(f'#{idx+1} {max_n} {max_cnt}')




