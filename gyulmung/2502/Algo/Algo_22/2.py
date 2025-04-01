strings = [list(map(str, input().split())) for _ in range(3)]

cnt = 0
if strings[0] == strings[1]:
    cnt += 1
if strings[1] == strings[2]:
    cnt += 1
if strings[0] == strings[2]:
    cnt += 1

if cnt == 3:
    print('WOW')
elif cnt == 2:
    print('GOOD')
else:
    print('BAD')