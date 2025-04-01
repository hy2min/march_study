N = int(input())
date_p = []
yesorno = ['x', 'o']

def date(lev):
    if lev == N:
        for i in range(lev):
            print(date_p[i], end ='')
        print()
        return

    for i in range(2):
        date_p.append(yesorno[i])
        date(lev + 1)
        date_p.pop()

date(0)