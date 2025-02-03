a = int(input())

def starBox():
    for i in range(1,21):
        if i % 2 == 1:
            print(i,end = ' ')

def macDoll():
    for i in range(ord("H"),ord("A")-1,-1):
        print(chr(i),end = ' ')

def copyBean():
    for i in range(-5,6):
        print(i, end = ' ')

if 3500 <= a <= 5000:
    starBox()
elif 2500 <= a <= 3500:
    macDoll()
else:
    copyBean()
