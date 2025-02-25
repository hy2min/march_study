lst = []
for _ in range(4):
    lst.append(input())
lst = sorted(lst, key=lambda x: len(x))
for i in lst:
    print(i)