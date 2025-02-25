lst = [i for i in map(int,input().split())]

a = 1
arr = []
for i in range(4):
    row = []
    for j in range(4):
        row.append(a)
        a += 1
    arr.append(row)

mod_arr = [[0] * 4 for _ in range(4)]
cnt = 1

def plus(num):

    global cnt

    for i in range(4):
        for j in range(4):
            if num == arr[i][j]:
                mod_arr[i][j] = cnt
                cnt += 1

for i in range(4):
    plus(lst[i])

for i in range(4):
    print(*mod_arr[i])