lst = []
for i in range(4):
    lst.append(input())

lst.sort(key=len)
for i in lst:
    print(i)