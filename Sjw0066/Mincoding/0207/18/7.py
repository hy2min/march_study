alphabet = [
	['A', 'B', 'C'],
    ['A', 'G', 'H'],
    ['H', 'I', 'J'],
    ['K', 'A', 'B'],
    ['A', 'B', 'C']
]

dat=[0]*100
sort_lst=[[0]*3 for _ in range(5)]

for i in range(len(alphabet)):
    for j in range(len(alphabet[i])):
        dat[ord(alphabet[i][j])] += 1

for i in range(1,len(dat)):
    dat[i] += dat[i-1]

for i in range(5):
    for j in range(3):
        index=ord(alphabet[i][j])
        dat[index] -= 1
        sort_lst[dat[index]//3][dat[index]%3]=chr(index)

for i in range(5):
    for j in range(3):
        print(sort_lst[i][j],end="")


