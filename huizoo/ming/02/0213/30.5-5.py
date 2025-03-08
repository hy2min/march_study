def backtracking(n):
    if n == pick:
        print(''.join(path))
        return
    for name in names:
        path.append(name)
        backtracking(n+1)
        path.pop()

names = input()
pick = int(input())
path = []
backtracking(0)
