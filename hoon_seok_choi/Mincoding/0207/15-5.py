a = input()
b = input()
c = input()
d = input()


arr = [[*a],[*b],[*c],[*d]]
arr2 = []

for i in range(4) :
    arr2.append(len(arr[i]))

arr2.sort(reverse=False)
for i in range(4) :
    print(arr2[i],end= " ")