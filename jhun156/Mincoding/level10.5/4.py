arr = [
    ['D','A','C','C','D'],
    ['S','D','F','A','E'],
    ['E','E','T','J','H'],
]

def Main():
    INPUT()

def INPUT():

    a = input()
    b = CHECK(a)

    if b == 1:
        print("있음")
    elif b == 0:
        print("없음")

def CHECK(chr):

    global arr

    for i in range(3):
        for j in range(5):
            if arr[i][j] == chr:
                return 1
    return 0
            
Main()
