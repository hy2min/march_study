N, M = map(int,input().split())
arr = [list(input().split()) for _ in range(M)]
lst = [[] for _ in range(N)]
for i in range(M):
    lst[int(arr[i][0])].append(arr[i][1])
revised_lst = list(enumerate(lst))  # 튜플로 묶임 (인덱스, 원래 값)
print(revised_lst)
revised_lst.sort(key = lambda x: (-len(x[1]),x[0]))
print(*revised_lst[0][1])