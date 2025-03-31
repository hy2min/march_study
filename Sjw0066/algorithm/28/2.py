N=int(input())

arr=[list(map(int,input().split())) for _ in range(N)]

boss=0
under=[]

for i in range(N):
    if arr[0][i]:
        under.append(i)
    for j in range(N):
        if arr[j][0]:
            boss=j

print(f'boss:{boss}')
print('under:',end="")
print(*under)