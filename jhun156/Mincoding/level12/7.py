arr = input()

a = input()
b = input()
c = input()
lst = [a,b,c]

for i in lst:
    count = arr.count(i)
    print(f"{i}={count}")