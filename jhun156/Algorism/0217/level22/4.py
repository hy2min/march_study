arr = []
for i in range(5):
    arr.append(input())

floor = [-5,-4,-3,-2,-1,1,2,3,4,5,6]
present = 5

for i in range(5):
    if arr[i] == 'up':
        present += 1
    else:
        present -= 1

if present >= 5:
    print(floor[present])
else:
    print(f"B{abs(floor[present])}")