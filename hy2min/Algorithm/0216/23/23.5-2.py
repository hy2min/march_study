people = [list(map(int,input().split())) for _ in range(3)]

flag = 0
for i in range(2):
    if people[0][i] == people[1][i] or people[0][i] == people[2][i] or people[1][i] == people[2][i]:
        flag = 1
if flag == 0:
    print('안전')
else:
    print('위험')