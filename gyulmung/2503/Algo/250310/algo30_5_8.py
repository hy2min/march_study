import sys
sys.stdin = open('input.txt', 'r')

arr = ['B', 'I', 'A', 'H']
N = int(input())
lst = []
num = 0
visited = [0]*4
for i in range(3):
    cnt = 0
    while 1:
        if num >= 4:
            num = 0
        if visited[num] == 1:
            num += 1
        elif cnt == N-1:
            lst.append(arr[num])
            visited[num] = 1
            num+=1
            break
        else:
            cnt += 1
            num += 1
for i in range(4):
    if visited[i] == 1:
        continue
    else:
        lst.append(arr[i])
print(*lst)