arr = [1, 1, 2, 3, 4, 5, 6, 1, 2, 3]
q = []
ret  = 0
count = 0
while arr:
    q.append(arr.pop(0))
    count += 1
    if len(set(q)) == len(q) - 2:
        ret = 1
        break
print(q)
print(count)
print(ret)
