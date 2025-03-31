name=['BTS','SBS','BS','CBS','SES']
target=input()
answer=0
path=['']*15
def dfs(level,str1):
    global answer

    if len(str1) > len(target):
        return

    if str1==target:
        answer=level
        return

    for i in range(5):
        path[level] = name[i]
        str2 = str1+path[level]
        dfs(level+1,str2)
        path[level] = ''

dfs(0,'')

print(answer)