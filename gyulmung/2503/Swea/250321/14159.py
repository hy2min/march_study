import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def Find(lst):
    cnt = 0
    for i in range(10):
        if lst.count(i) >= 3:
            return 1
        if lst.count(i) >= 1:
            cnt += 1
        else:
            cnt = 0
        if cnt >= 3:
            return 1
    return 0



T = int(input())

for test in range(1, T+1):
    arr = list(map(int, input().split()))
    card = deque()
    for i in arr:
        card.append(i)
    player1 = []
    player2 = []
    ret1, ret2 = 0, 0
    while 1:
        if not card:
            print(f'#{test} {0}')
            break
        if len(player1) <2:
            player1.append(card.popleft())
            player2.append(card.popleft())
        else:
            player1.append(card.popleft())
            ret1 = Find(player1)
            if ret1:
                print(f'#{test} {1}')
                break
            player2.append(card.popleft())
            ret2 = Find(player2)
            if ret2:
                print(f'#{test} {2}')
                break
