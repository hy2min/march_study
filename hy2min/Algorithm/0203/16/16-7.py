flag = False

for _ in range(3):
    string = input()
    if 'M' in string:
        flag = True
            
if flag:
    print('M이 존재합니다')
else:
    print('M이 존재하지 않습니다')    