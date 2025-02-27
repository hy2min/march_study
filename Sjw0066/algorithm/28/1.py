name=['Amy','Bob','Chloe','Edger','Diane']

arr=[
    [0,0,0,1,0],
    [1,0,0,0,0],
    [0,1,0,0,0],
    [0,1,0,0,0],
    [0,0,0,0,1],
]

Max=0

for i in range(5):
    cnt=0
    for j in range(5):
        if arr[j][i] == 1 :
            cnt+=1
    if cnt>Max:
        Max=cnt
        famous=name[i]

print(famous)
