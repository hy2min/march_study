# import sys
# sys.stdin = open("input.txt","r")

p = list(map(int,input().split()))
q = list(map(int,input().split()))
result = []
tmp = 0

while 1:
    if p[0] < q[0]:
        result.append(p.pop(0))
    else:
        result.append(q.pop(0))

    if not p:
        tmp = q
        break
    elif not q:
        tmp = p
        break

while tmp:
    result.append(tmp.pop(0))

print(*result)