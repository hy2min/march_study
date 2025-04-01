stop = input()
name = 'ABCD'
path = []
# str_path = ''
cnt = 1

def abc(lev):
    global path, cnt

    str_path = ''.join(path)
    if str_path == stop:
        print(f'{cnt}번째')

    if lev == 3:
        cnt += 1
        return

    for i in range(4):
        path.append(name[i])
        abc(lev + 1)
        path.pop()
abc(0)