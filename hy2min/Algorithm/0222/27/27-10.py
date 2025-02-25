a = [
    [2,6,3],
    [7,1,1],
    [3,4,2],
]
b = [
    [6,4,2,4],
    [1,1,5,8],
]
c = [
    [9,2,3],
    [4,2,1],
]
arr = []

a_flat = [num for row in a for num in row]
a_flat.sort(reverse=True)
b_flat = [num for row in b for num in row]
b_flat.sort()
c_flat = [num for row in c for num in row]
c_flat.sort()

arr.append(a_flat[:3])
arr.append(b_flat[:3])
arr.append(c_flat[:2]+[c_flat[-1]])

for i in arr:
    for j in i:
        print(j, end=" ")
    print()
