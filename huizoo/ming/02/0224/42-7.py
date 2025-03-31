st = list(input())
n = int(input())
st2 = 'abcdefg'
arr = [15, 20, 44, 22, 55, 16, 45]
Sum = 0
for i in st:
    Sum += arr[st2.index(i)]
Max = 0
used = [0]*len(st)
def dfs(x, Sum2):
    global Max
    if x == n:
        if Sum2 % 10 == 0:
            Max = max(Sum2, Max)
        return
    for i in range(len(st)):
        if not used[i]:
            used[i] = 1
            dfs(x+1, Sum2-arr[st2.index(st[i])])
            used[i] = 0

dfs(0, Sum)
print(Max)