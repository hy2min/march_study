name = ['A', 'B', 'C', 'Z', 'E', 'T', 'Q']
blacklist = input()

for i in blacklist:
    flag = True
    for j in name:
        if i == j:
            flag = False
    if flag:
        print(f'{i}=외부사람')
    else:
        print(f'{i}=마을사람')
