import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
password = {'13': 0, '25': 1, '19': 2, '61': 3, '35': 4, '49': 5, '47': 6, '59': 7, '55': 8, '11': 9}
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
print(arr)
lst = []
for i in range(1,n):
    for j in range(m-1, -1, -1):
        if arr[i][j] == '1':
            for k in range(8):
                lst.append(arr[i][(j-7*k)-6:(j-7*k)+1])
        if lst:
            break
print(lst)
ret = []

for i in range(len(lst)):
    a = ''.join(lst[i])
    ret.append(a)
print(ret)

backup = []
while ret:
    backup.append(ret.pop())
print(backup)

result = [0]
for i in range(8):
    a = str(int(backup[i], 2))
    b = password.get(a)
    result.append(b)
print(result)

result_odd = []
result_even = []
for i in range(1, len(result)):
    if i % 2 != 0:
        result_odd.append(result[i])
    else:
        result_even.append(result[i])
if (sum(result_odd)*3+sum(result_even)) % 10 == 0:
    ans = sum(result)
print(ans)
