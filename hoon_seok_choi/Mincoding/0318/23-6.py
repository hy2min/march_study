card = list(map(int, input()))

path = [0] * 4
cnt = 0

def recur(depth):
    global cnt
    if depth == 4:
        cnt += 1
        return
    
    for i in card:
        if depth == 0 or abs(path[depth - i] - i) <= 3 :
            path[depth] = i
            recur(depth + 1)

recur(0)
print(cnt)