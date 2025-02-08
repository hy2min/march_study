yx_lst = []
for i in range(4):
    yx_lst.extend(map(int,input().split()))

vect = [[0] * 3 for _ in range(4)]

for i in range(0,8,2):
    vect[yx_lst[i]][yx_lst[i+1]] = 5

for i in range(4):
    print(*vect[i])