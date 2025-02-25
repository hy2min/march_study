# import sys
# sys.stdin = open("input.txt","r")

st_y = st_x = ed_y = ed_x = 0
arr=[list(map(int,input().split())) for _ in range(4)]

for i in range(4):
    for j in range(5):
        if st_y == 0 and st_x == 0 and arr[i][j] == 1:
            st_y,st_x = i,j
        if arr[i][j] == 1:
            ed_y,ed_x = i,j

print(f"({st_y},{st_x})")
print(f"({ed_y},{ed_x})")