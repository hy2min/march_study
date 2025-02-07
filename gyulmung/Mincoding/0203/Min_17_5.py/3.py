name1 = input()
name2 = input()

def isSame():
    if name1 == name2:
        return 1
    else:
        return 0

if isSame():
    print('동명')
else:
    print('남남')