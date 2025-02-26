arr = [[3, 5, 1], [4, 2, 6]]
people = list(map(int, input().split()))

lst = [0]*10

for i in range(2):
    for j in range(3):
        lst[arr[i][j]] += 1

for j in range(len(people)):
        if lst[people[j]] != 0:
            print(f'{people[j]}번 합격')
        else:
            print(f'{people[j]}번 불합격')