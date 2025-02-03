a = int(input())
arr = [i for i in input().split()]
lst = []

for i in range(a):
    lst.append(arr[i])

for i in lst:
    print(i,end='')