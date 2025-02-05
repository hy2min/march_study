arr = []
n =1
for i in range(7):
    row = []
    for j in range(4):
        row.append(n)
        n+=1
    arr.append(row)

a, b, c = map(int, input().split())

for i in range(7):
    for j in range(4):
        if i == a or i==b or i==c:
            arr[i][j]= 0
    print(*arr[i])