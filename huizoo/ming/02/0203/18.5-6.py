win = [
    [3,5,1],
    [4,2,6],
]

people = list(map(int, input().split()))

dat = [0] * 10

for row in win : 
    for num in row : 
        dat[num] += 1

for person in people : 
    if dat[person] : 
        print(f'{person}번 합격')
    else : 
        print(f'{person}번 불합격')