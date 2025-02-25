win = [
    [3,5,1],
    [4,2,6],
]
people = [i for i in map(int,input().split())]

def find_success(num):
    for i in range(2):
        for j in range(3):
            if win[i][j] == num:
                return 1
    return 0

for i in range(4):
    ans = find_success(people[i])
    if ans == 1:
        print(f"{people[i]}번 합격")
    else:
        print(f"{people[i]}번 불합격")