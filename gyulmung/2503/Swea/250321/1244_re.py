import sys
sys.stdin = open('input.txt','r')

def rotation(lev, lst):
    global Max
    if lev == rotate:
        ret = int("".join(lst))
        Max = max(Max,ret)
        visited.add(Max)
        return

    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if "".join(lst) not in visited:
                lst[i], lst[j] = lst[j], lst[i]
                rotation(lev+1, lst)
                lst[i], lst[j] = lst[j], lst[i]

T = int(input())
for test in range(1, T+1):
    input_num = input().split()
    number, rotate = input_num
    number = list(number)
    rotate = int(rotate)
    visited = set()
    Max = -1e8

    rotation(0, number)
    print(Max)
