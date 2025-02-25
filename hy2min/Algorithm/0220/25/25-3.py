lst = list(input().split('_'))
ret = []
for i in lst:
    if i != '':
        ret.append(i)
for i in range(len(ret)):
    print(f'{i+1}#{ret[i]}')