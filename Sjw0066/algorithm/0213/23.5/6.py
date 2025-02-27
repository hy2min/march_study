arr1=[list(input()) for _ in range(4)]
arr2=[
    ['A','B','C','D'],
    ['B','B','A','B'],
    ['C','B','A','B'],
    ['B','A','A','A'],
]

max_cnt=-21e8
answer=0
for i in range(4):
    cnt=0
    for j in range(4):
        for k in range(4):
            if arr2[j][k] == arr1[j][k] and arr2[j][k] == chr(65+i):
                cnt+=1
    if cnt>max_cnt:
        max_cnt=cnt
        answer=65+i

print(chr(answer))
