P = int(input())
for i in range(P):
    tc, *lst = map(int, input().split())
    cnt = 0
    for i in range(19, -1, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                cnt += 1
    print(tc, cnt)