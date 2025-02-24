win = [
    [3,5,1],
    [4,2,6],
]
people = list(map(int, input().split()))
for person in people:
    if person in win[1] or person in win[0]:
        print(f'{person}번 합격')
    else: 
        print(f'{person}번 불합격')