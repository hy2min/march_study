n = int(input())
string = 'ABC'
path = [0] * n
cnt = 0

def abc(level):
    global cnt,string

    if level == n:
        for i in range(3):
            for j in range(n-2):
                if path[j] == path[j+1] == path[j+2] == string[i]:
                    return
        cnt += 1
        return

    for i in range(3):
        path[level] = string[i]
        abc(level+1)

abc(0)
print(cnt)