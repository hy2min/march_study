word2 = input()
word = list(word2)
cnt = 0
path = [0]*4

def recur(depth):
    global cnt
    if depth == 4:
        current = ''.join(path)
        if 'BT' not in current and 'TB' not in current:
            cnt += 1
        return

    for i in range(4):
        path[depth] = word[i]
        recur(depth+1)
        

recur(0)
print(cnt)