


arr2 = [[0]*3 for _ in range(6)]
a = ord('A')

b = 0

for j in range(2,-1,-1) :
    for i in range(5,-1,-1) :
        arr2[i][j] = chr(a)
        a+=1
# print(arr2)

c,d = map(int, input().split())

print(arr2[c][d])