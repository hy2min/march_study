arr = list(input())

if 'B' in arr and 'T' in arr:
    b = arr.index('B')
    t = arr.index('T')
    cnt = 0
    path = [0]*4

    def abc(level):

        global cnt

        if level == 4:
            cnt += 1
            return

        for i in range(4):
            if level >= 1 and path[level-1] == 'B' and i == t: continue
            if level >= 1 and path[level-1] == 'T' and i == b: continue
            path[level] = arr[i]
            abc(level+1)
            path[level] = 0

    abc(0)
    print(cnt)

else:
    cnt = 256
    print(cnt)
