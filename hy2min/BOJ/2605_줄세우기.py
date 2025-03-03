N = int(input())
lst = list(map(int, input().split()))
a_lst = list(range(1, N+1))

for i in range(N):
    n, t = lst[i], a_lst[i]
    for j in range(i, i-n, -1):
        a_lst[j] = a_lst[j-1]
    a_lst[i-n] = t
print(*a_lst)