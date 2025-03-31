st = 1
ed = 50
N = int(input())
arr = [list(input().split()) for _ in range(N)]
flag = 0
for i in range(N):
    if arr[i][1] == 'DOWN':
        ed = int(arr[i][0]) - 1
    else:
        st = int(arr[i][0]) + 1
    if st > ed:
        flag = 1
        break

if flag:
    print("ERROR")
else:
    if st == ed:
        print(st)
    else:
        print(f"{st} ~ {ed}")