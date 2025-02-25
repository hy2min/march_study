arr1 = [[0] * 5 for _ in range(2)]
arr2 = [
    [3,5,4,1,1],
    [3,5,2,5,6],
]

a = int(input())

lst = []
for i in range(2,5):
    lst.append(arr2[1][i])
lst.append(arr2[0][2])

if a in lst:
    print(f"{a} 존재")
else:
    print(f"{a} 없음")