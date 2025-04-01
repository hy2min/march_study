import sys
sys.stdin=open('input.txt','r')

n = int(input())
arr = list(map(int, input().split()))
bomb = []
bomb.append(arr.pop(0))
while arr:
    if len(arr) >= 3:
        if bomb[-1] == arr[0] and bomb[-1] == arr[1]:
            bomb.pop()
            arr.pop(0)
            arr.pop(0)
    bomb.append(arr.pop(0))
print(*sorted(bomb))
