a = list(input())
N = len(a)
n = int(input())
used = [0] * N

things = {
    'a' : 15,
    'b' : 20,
    'c' : 44,
    'd' : 22,
    'e' : 55,
    'f' : 16,
    'g' : 45,
}

Max = -100
Sum = 0
for i in a:
    Sum += things[i]

def dfs(level,price):
    global Max
    if level == n and price % 10 == 0:
        Max = max(Max,price)
        return

    for i in range(N):
        if used[i] == 0:
            used[i] = 1
            dfs(level+1,price-things[a[i]])
            used[i] = 0

dfs(0,Sum)
print(Max)