arr = [
    ['a','b','d'],
    ['e','w','z'],
    ['q','v','a'],
]

def Input():
    a = input()
    rnt = Process(a)
    if rnt > 0:
        print("존재")
    else:
        print("없음")

def Process(chr):
    CHR = chr.lower()
    result = 0

    for i in range(3):
        count = arr[i].count(CHR)
        result += count
    return result

Input()