a = input()
b = input()
c = input()
d = input()

arr = [a,b,c,d]
arr.sort(key=len)

for i in arr:
    print(i)