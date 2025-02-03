arr = [i for i in input().split()]

def checkChar(a):
    if a.isupper():
        print("대",end='')
    else:
        print("소",end='')

for i in arr:
    checkChar(i)

