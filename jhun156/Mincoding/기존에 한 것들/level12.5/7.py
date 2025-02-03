lst = []
arr = []

for i in range(3):
    a = input()
    lst.append(a)
    arr.append(len(a))

mm = max(arr)

for i in range(3):
    if len(lst[i]) == mm:
        print(lst[i])