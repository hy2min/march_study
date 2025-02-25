win = [
    [3, 5, 1],
    [4, 2, 6],
]
people = list(map(int, input().split()))

for person in people:
    for check in win:
        if person in check:
            print(f'{person}번 합격')
            break
    else:
        print(f'{person}번 불합격')
