import copy, sys

input = sys.stdin.readline

def abc(level, lst):
    global Max
    if level == 5:
        for row in lst:
            Max = max(Max, max(row))
        return
    for i in range(4):
        lst2 = copy.deepcopy(lst)
        if i == 0:  # 동
            for j in range(N):
                top = N-1
                for k in range(N-2, -1, -1):
                    if lst2[j][k] == 0:
                        continue
                    if lst2[j][top] == lst2[j][k]:
                        lst2[j][top] *= 2
                        lst2[j][k] = 0
                        top -= 1
                    elif lst2[j][top] == 0:
                        lst2[j][top], lst2[j][k] = lst2[j][k], lst2[j][top]
                    else:
                        top -= 1
                        lst2[j][top], lst2[j][k] = lst2[j][k], lst2[j][top]
            abc(level+1, lst2)
        elif i == 1:    # 서
            for j in range(N):
                top = 0
                for k in range(1, N):
                    if lst2[j][k] == 0:
                        continue
                    if lst2[j][top] == lst2[j][k]:
                        lst2[j][top] *= 2
                        lst2[j][k] = 0
                        top += 1
                    elif lst2[j][top] == 0:
                        lst2[j][top], lst2[j][k] = lst2[j][k], lst2[j][top]
                    else:
                        top += 1
                        lst2[j][top], lst2[j][k] = lst2[j][k], lst2[j][top]
            abc(level + 1, lst2)
        elif i == 2:    # 남
            for k in range(N):
                top = N-1
                for j in range(N-2, -1, -1):
                    if lst2[j][k] == 0:
                        continue
                    if lst2[top][k] == lst2[j][k]:
                        lst2[top][k] *= 2
                        lst2[j][k] = 0
                        top -= 1
                    elif lst2[top][k] == 0:
                        lst2[top][k], lst2[j][k] = lst2[j][k], lst2[top][k]
                    else:
                        top -= 1
                        lst2[top][k], lst2[j][k] = lst2[j][k], lst2[top][k]
            abc(level + 1, lst2)
        else:   # 북
            for k in range(N):
                top = 0
                for j in range(1, N):
                    if lst2[j][k] == 0:
                        continue
                    if lst2[top][k] == lst2[j][k]:
                        lst2[top][k] *= 2
                        lst2[j][k] = 0
                        top += 1
                    elif lst2[top][k] == 0:
                        lst2[top][k], lst2[j][k] = lst2[j][k], lst2[top][k]
                    else:
                        top += 1
                        lst2[top][k], lst2[j][k] = lst2[j][k], lst2[top][k]
            abc(level + 1, lst2)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
Max = 0
abc(0, arr)
print(Max)