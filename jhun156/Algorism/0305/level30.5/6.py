# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    pw = input()
    path = [0] * 4
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cnt = 0

    def dfs(level):

        global cnt
        if level == 4:
            cnt += 1
            tmp = ''
            for i in range(4):
                tmp += path[i]
            if tmp == pw:
                print(cnt)
                return
            return

        for i in range(26):
            path[level] = abc[i]
            dfs(level + 1)

    dfs(0)