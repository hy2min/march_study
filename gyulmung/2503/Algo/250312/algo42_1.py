import sys
sys.stdin=open('input.txt','r')

arr = input()
path = []

for i in range(len(arr)):
    for j in range(i, len(arr)):
        for k in range(j, len(arr)):
            path.append((arr[i], arr[j], arr[k]))
for i in range(len(path)):
    ret = ''.join(path[i])
    print(ret)