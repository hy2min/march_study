name=['A','B','C','D','E','F','G','H']
arr=[
    [0,1,1,0,0,0,0,1],
    [0,0,0,0,0,0,0,0],
    [0,0,0,1,1,0,1,0],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
]

target=input()
target_index=ord(target)-ord('A')

parents=-1
brother=[]
for i in range(8):
    if arr[i][target_index] == 1:
        parents=i

if parents == -1:
    print('없음')
else:
    for i in range(8):
        if arr[parents][i] == 1 and i != target_index:
            brother.append(i)
            print(chr(65+i),end=" ")
    if brother == []:
        print('없음')