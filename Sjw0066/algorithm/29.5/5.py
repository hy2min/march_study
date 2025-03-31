arr=[list(map(int,input().split())) for _ in range(4)]

st=[]
ed=[]
for i in range(4):
    for j in range(5):
        if arr[i][j] == 1 :
            st=[i,j]
            break
    if st:
        break

for i in range(3,-1,-1):
    for j in range(4,-1,-1):
        if arr[i][j]==1:
            ed=[i,j]
            break
    if ed:
        break

print(f'({st[0]},{st[1]})')
print(f'({ed[0]},{ed[1]})')
