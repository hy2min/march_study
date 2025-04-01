import sys
sys.stdin = open('input.txt', 'r')

import copy
arr = list(input())
n = int(input())
length = len(arr)
Max = -1e8
def change(lev, lst):
    global Max, arr
    if lev == n:
        Sum = 0
        for i in range(length-1):
            # 이웃한 글자가 같을 때
            if arr[i] == arr[i + 1]:
                Sum -= 50
            elif abs(ord(arr[i]) - ord(arr[i + 1])) <= 5:
                Sum += 3
            elif abs(ord(arr[i]) - ord(arr[i + 1])) >= 20:
                Sum += 10
        if Max < Sum:
            Max = Sum
        return

    for i in range(length):
        for j in range(i+1, length):
            lst = copy.deepcopy(arr)
            arr[i], arr[j] = arr[j], arr[i]
            change(lev+1, lst)
            arr = lst
lst = []
change(0, lst)
print(Max)
