arr = list(input())
N = int(input())

arr.sort(key= lambda x:-ord(x))
lst = arr[:N]
dict = {}
for i in range(N):
    dict[lst[i]] = lst.count(lst[i])

for key,item in dict.items():
    if item == max(dict.values()):
        print(key)