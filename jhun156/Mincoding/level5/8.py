a = 0

def KFC():
    global a
    a = int(input())

def BBQ():
    if a > 5:
        print("만세")
    else:
        print("다시")

KFC()
BBQ()