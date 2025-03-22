# 4 x 8 size
arr = [list(map(int,input().split())) for _ in range(4)]
st_y = 0
for i in range(4):
    if 0 not in arr[i]:
        st_y = i
        break
ed_y = 0
for i in range(3,-1,-1):
    if 0 not in arr[i]:
        ed_y = i
        break
mod_arr = []
for i in range(st_y,ed_y+1):
    mod_arr.append(arr[i])

lst = list(zip(*mod_arr))

st_x = 0
for i in range(len(lst)):
    if 0 not in lst[i]:
        st_x = i
        break

ed_x = 0
for i in range(len(lst)-1,-1,-1):
    if 0 not in lst[i]:
        ed_x = i
        break

Sum = 0
for i in range(st_x,ed_x+1):
    for j in range(ed_y-st_y+1):
        Sum += lst[i][j]

print(Sum)