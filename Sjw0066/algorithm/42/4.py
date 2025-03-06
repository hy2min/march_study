coin=[10,40,60]
target=int(input())
answer=21e8
def dfs(cnt,Sum):
    global answer

    if Sum>target:
        return

    if Sum==target:
        if answer>cnt:
            answer=cnt
        return

    for i in range(3):
        dfs(cnt+1,Sum+coin[i])

dfs(0,0)
print(answer)