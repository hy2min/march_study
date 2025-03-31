arr = [list(map(int,input().split())) for _ in range(4)]


arr2 = []

for i in range(4):
    for j in range(5):
        if arr[i][j]==1 :
            arr2.append((i,j))

min_x,min_y = arr2[0]
max_x,max_y = arr2[-1]

print(f"({min_x},{min_y})")
print(f"({max_x},{max_y})")
