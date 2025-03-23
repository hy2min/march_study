N = int(input())
dic = dict()
for _ in range(N):
    a, b = input().split()
    if a in dic:
        print(a)
        print(min(dic[a], b), max(dic[a], b))
    else:
        dic[a] = b