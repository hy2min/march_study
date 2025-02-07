a =input()

arr = [*a]
arr2 = []
arr3 = []

for i in range(len(arr)) :
    arr2.append(ord(arr[i]))


arr2.sort()

for i in range(len(arr2)) :
    arr3.append(chr(arr2[i]))

print(*arr3,end="",sep="")
