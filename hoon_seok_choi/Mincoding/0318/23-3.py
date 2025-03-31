name = ['A', 'B', 'C']

n = int(input())
path = [0]*n

cnt = 0

def recur(depth):
    global cnt
    if depth == n:
        for i in range(n - 2):
            if path[i] == path[i + 1] == path[i + 2]:
                return
        cnt += 1
        return
    for i in name:
        path[depth] = i
        recur(depth+1)

recur(0)
print(cnt)