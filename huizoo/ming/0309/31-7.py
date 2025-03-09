# n = int(input())
# arr = sorted([input() for _ in range(n)], key=lambda x: (len(x), x))
# for st in arr:
#     print(st)

n = int(input())
arr = []
for _ in range(n):
    st = input()
    length = len(st)
    flag = 0
    for i in range(len(arr)):
        if length > len(arr[i]):continue
        if length == len(arr[i]):
            if st < arr[i]:
                arr.insert(i, st)
                flag = 1
                break
            continue
        arr.insert(i, st)
        flag = 1
        break
    if flag: continue
    arr.append(st)
for st in arr:
    print(st)