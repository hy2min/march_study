n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    if arr[i][0] == 1:
        print(f'boss:{i}')

under = []
for i in range(n):
    if arr[0][i] == 1:
        under.append(i)
print(f'under:{" ".join(map(str,under))}')