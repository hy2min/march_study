choco = ['A', 'B', 'C']
n = int(input())
path = []

# cnt = 0
# def dfs(level, max_level) : 
#     global cnt
#     if level == max_level : 
#         cnt += 1
#         return
#     for chocolate in choco : 
#         path.append(chocolate)
#         if 'AAA' in ''.join(path) or 'BBB' in ''.join(path) or 'CCC' in ''.join(path) : 
#             pass
#         else : 
#             dfs(level+1, max_level)
#         path.pop()
# dfs(0,n)
# print(cnt)

def dfs(level, max_level) : 
    if level == max_level : 
        return 1
    cnt = 0
    for chocolate in choco : 
        if len(path) >= 2 and path[-2:] == [chocolate, chocolate] : 
            continue
        path.append(chocolate)
        cnt += dfs(level+1, max_level)
        path.pop()
    return cnt

ret = dfs(0,n)
print(ret)