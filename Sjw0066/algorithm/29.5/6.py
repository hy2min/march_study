arr=[
    [3,2,5,3],
    [7,6,1,6],
    [4,9,2,7],
]

answer=[[0]*4 for _ in range(3)]
lst1=list(map(int,input().split()))

for i in range(4):
    for j in range(3):
        roll=lst1[i]
        nj=(j+roll%3)%3
        answer[nj][i] = arr[j][i]

for i in answer:
    print(*i,sep="")
