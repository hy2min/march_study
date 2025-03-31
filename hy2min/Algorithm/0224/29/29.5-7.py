arr = ['_'] * 5
idx, age = map(int, input().split())

def dfs(i, age):
    if i > 4 or age == 0:
        print('_____')
        return
    arr[i] = age
    print("".join(map(str,arr)))
    arr[i] = '_'
    dfs(i+1, age-1)

dfs(idx,age)