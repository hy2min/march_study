import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
coin = [(0)]
for i in range(n):
    value = int(input())
    coin.append(value)
coin.sort()
lst = [[1e8]*(m+1) for _ in range(n+1)]
print(lst)
print(coin)

for i in range(1, n+1):
    for j in range(1, m+1):
        if j % coin[i] == 0:
            lst[i][j] = j//coin[i]
        else:
            if j // coin[i] == 0:
                lst[i][j] = lst[i-1][j]
            else:
                lst[i][j] = min(lst[i-1][j], 1 + lst[i-1][j-coin[i]])

print(lst[-1][m])
