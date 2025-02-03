strr = list("DATAPOWER")

a,b = map(int,input().split())

lst = [0] * 9
count = 0

for i in range(a,b+1):
    lst[count] = strr[i]
    count += 1

for i in range(b-a+1):
    print(lst[i],end='')