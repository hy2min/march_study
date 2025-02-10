T = int(input())
for idx in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    arr = []
    lst.sort()
    for i in range(N//2):
        arr.append(lst[-(i+1)])
        arr.append(lst[i])


    print(f'#{idx+1} {" ".join(map(str,arr[:10]))}')
