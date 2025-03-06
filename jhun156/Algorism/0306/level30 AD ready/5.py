# import sys
# sys.stdin = open("input.txt","r")

y,x = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(y)]
lst = []

for i in range(y):
    for j in range(x):
        lst.append([arr[i][j],i,j])

lst.sort(key = lambda x : (-x[0], x[1], x[2]))
for i in range(3):
    print(f"{lst[i][0]}({lst[i][1]},{lst[i][2]})")