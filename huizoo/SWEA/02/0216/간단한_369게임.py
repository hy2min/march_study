n = int(input())
for i in range(1, n+1):
    a = str(i)
    if '3' in a or '6' in a or '9' in a:
        m = a.count('3')+a.count('6')+a.count('9')
        print('-'*m, end=' ')
    else: print(i, end=' ')