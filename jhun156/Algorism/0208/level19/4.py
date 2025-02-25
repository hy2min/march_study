arr1 = [i for i in map(int,input().split())]
arr2 = [i for i in map(int,input().split())]

lst = list(zip(arr1,arr2))
for i in range(3):
    print(sum(lst[i]))