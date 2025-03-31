n = int(input())
def abc(i):
    if i == 0:
        return
    abc(i//2)
    print(i, end = ' ')
abc(n)