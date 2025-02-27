train = [3, 7, 6, 4, 2, 9, 1, 7]
team = list(map(int, input().split()))

# 1. team 1번 인덱스가 어디있는지 확인 - 함수처리

def Find_team(i):
    count = 0
    for seat in range(3):
        if train[i + seat] == team[0 + seat]:
            count = i + seat
    return count

# 2. 1번 인덱스 찾았으면 뒤에도 맞는지 확인
for i in range(6):
    if train[i] == team[0]:
        first_team = i
        final_team = Find_team(i)


print(f'{first_team}번~{final_team}번 칸')