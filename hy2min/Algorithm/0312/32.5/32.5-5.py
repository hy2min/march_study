arr = [3,2,-1,3,-2,0,-1]

def dfs(level):
    if level == 5:
        print(f'{level}번')
        return
    dfs(level + arr[level])
    print(f'{level}번')

n = int(input())
dfs(n)
