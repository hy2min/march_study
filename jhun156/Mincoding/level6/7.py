a = int(input())

arr = ["#" for i in range(a)]

for i in range(a):
    for j in arr:
        print(j,end='')
    print()
