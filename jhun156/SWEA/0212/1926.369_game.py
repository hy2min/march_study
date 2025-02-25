def game(num):
    a = str(num)
    lst = list(map(int,a))
    n = len(lst)
    cnt = 0
    for i in range(n):
        if lst[i] == 3 or lst[i] == 6 or lst[i] == 9:
            cnt += 1
    if cnt == 2:
        print('--',end=' ')
    elif cnt == 1:
        print('-',end=' ')
    else:
        print(num,end=' ')

N = int(input())
for i in range(1,N+1):
    game(i)