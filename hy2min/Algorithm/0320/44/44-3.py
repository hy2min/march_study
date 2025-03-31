mos = ['1011','0011','1111','0000','1100']
flag = 0
for _ in range(5):
    signal = input()
    for m in mos:
        if m in signal:
            flag = 1

if flag:
    print('yes')
else:
    print('no')

