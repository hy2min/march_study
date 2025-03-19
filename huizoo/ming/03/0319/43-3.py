st = 'BOBOOBOBOBOBBM'

dic = dict()
for i in range(len(st)-2):
    now = st[i:i+3]
    if now in dic:
        dic[now] += 1
    else:
        dic[now] = 1

n = int(input())
for _ in range(n):
    print(dic.get(input(), 0))
