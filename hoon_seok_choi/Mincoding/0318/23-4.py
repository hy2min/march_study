member = ['B', 'T', 'S', 'K', 'R']
n = int(input())

path = [0]*n
used = [0]*len(member)
cnt = 0

#반드시 S를 포함시켜야함

def recur(depth):
    global cnt
    if depth == n :
        if 'S' in path:
            cnt += 1
        return
    
    for i in range(len(member)):
        if used[i] == 0:
            used[i] = 1 
            path[depth] = member[i] 
            recur(depth + 1)
            used[i] = 0

recur(0)
print(cnt)