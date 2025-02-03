arr = [
    [1,None,None,None,None],
    [1,None,1,None,None],
    [1,1,None,1,None],
    [1,None,1,None,None],
    [None,1,None,None,1],
    [None,None,None,1,None],
    [1,1,None,None,None],
]

def Main():
    rnt = PROCESS(INPUT())
    OUTPUT(rnt)

def INPUT():
    number = int(input())
    return number

def PROCESS(a):
    count = 0
    for i in range(7):
        if arr[i][a] == 1:
            count += 1
    return count

def OUTPUT(a):
    print(a)

Main()

