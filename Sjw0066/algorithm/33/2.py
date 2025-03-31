arr=[
    ['A','B','C'],
    ['D','E','F'],
    ['H','G'],
    ['I','J'],
]

N=int(input())

for i in range(N):
    ain=0
    bin=0
    a,b=input().split()
    for j in range(len(arr)):
        if a in arr[j]:
            ain=j
        if b in arr[j]:
            bin=j

    if  ain != bin:
        arr[ain]+=arr[bin]
        arr.pop(bin)

print(f'{len(arr)}개')

