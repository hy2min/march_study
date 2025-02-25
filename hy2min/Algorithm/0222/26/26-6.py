arr = []
flag= 1
for _ in range(6):
    x,y = map(int, input().split())
    if (x,y) in arr:
        flag = 0
        break
    arr.append((x,y))
if flag:
    print('중복없음')
else:
    print('중복된좌표발견')