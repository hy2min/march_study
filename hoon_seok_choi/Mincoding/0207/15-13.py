arr = [
    ['D','A','T','A','W'],
    ['B','B','Q','K']
]

A = int(input())

if A%2 ==1 :
    arr[0].sort(reverse=False)
else :
    arr[1].sort(reverse=False)
    

for i in range(2) :
    for j in arr[i] :
        print(j, end="")
    print()