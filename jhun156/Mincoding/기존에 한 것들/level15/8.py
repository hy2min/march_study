lst = []
for i in range(5):
    a = input()
    lst.append(a)

lst.sort(key = len,reverse = True)
print(lst[0])