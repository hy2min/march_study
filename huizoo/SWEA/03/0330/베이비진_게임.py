import sys
sys.stdin = open("input.txt", "r")

def is_babygin(lst):
    if max(lst) >= 3: return 1
    l = len(lst)
    for i in range(2, l):
        if lst[i] != 0 and lst[i-1] != 0 and lst[i-2] != 0:
            return 1

    return 0

def start():
    for i in range(12):
        if i % 2 == 0:
            one[arr[i]] += 1
            if i >= 5:
                if is_babygin(one):
                    return 1
        else:
            two[arr[i]] += 1
            if i >= 6:
                if is_babygin(two):
                    return 2

    return 0

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    one = [0]*10
    two = [0]*10
    print(f'#{tc} {start()}')
