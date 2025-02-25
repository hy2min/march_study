a = input()
arr = list(map(int,a))
path = [0] * 4
cnt = 0

def card(level):
    global cnt
    if level == 4:
        cnt += 1
        return

    for i in range(5):
        if level == 0:
            path[level] = arr[i]
        else:
            if abs(path[level-1] - arr[i]) > 3:
                continue
            else:
                path[level] = arr[i]
        card(level+1)

card(0)
print(cnt)