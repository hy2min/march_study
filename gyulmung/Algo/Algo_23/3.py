import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
choco = 'ABC'
path = [0]*n
count = 0

def abc(lev):
    global path, count
    if lev == n:
        count += 1
        return


    for i in range(3):
        path[lev] = choco[i]
        # lev 2로 해야 path 인덱스의 2와 0,1을 비교할 수 있다다
        if lev >= 2:
            if path[lev-2] == path[lev] and path[lev-1] == path[lev]:
                continue

        abc(lev + 1)

    return count

# 다른 방법 - 희주
# result = abc(0)
# print(result)
#
# choco = ['A', 'B', 'C']
# n = int(input())
# path = []
#
#
# def dfs(level, max_level) :
#     if level == max_level :
#         return 1
#     cnt = 0
#     for chocolate in choco :
#         if len(path) >= 2 and path[-2:] == [chocolate, chocolate] :
#             continue
#         path.append(chocolate)
#         cnt += dfs(level+1, max_level)
#         path.pop()
#     return cnt
#
# ret = dfs(0,n)
# print(ret)

# DFS
# def dfs(a):
#     global cnt
#     if a >= 3:
#         st = ''.join(path)
#         if 'AAA' in st or 'BBB' in st or 'CCC' in st:
#             return
#     if a == n:
#         cnt+=1
#         return
#     for i in 'ABC':
#         path.append(i)
#         dfs(a+1)
#         path.pop()
#
# n = int(input())
# path = []
# cnt = 0
# dfs(0)
# print(cnt)