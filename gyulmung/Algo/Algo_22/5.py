n = int(input())
seq = [0]*4

def clean(lev):
    if lev == 4:
        for i in range(lev):
            print(seq[i], end = '')
        print()
        return

    for i in range(1, n+1):
        seq[lev] = i
        clean(lev + 1)
        seq[lev] = 0

clean(0)