# 빙고가 3개 이상인지 확인
def check_bingo(user):
    cnt = 0
    for row in user:
        if row.count(0) == 5:
            cnt += 1

    for col in list(map(list, zip(*user))):
        if col.count(0) == 5:
            cnt += 1

    if all(user[i][i] == 0 for i in range(5)):
        cnt += 1
    if all(user[i][4-i] == 0 for i in range(5)):
        cnt += 1

    if cnt >= 3:
        return 1

user = [list(map(int, input().split())) for _ in range(5)]
mc = [num for _ in range(5) for num in map(int,input().split())]

# 숫자가 불렸을 때 0 처리
for turn, call in enumerate(mc,1):
    for i in range(5):
        for j in range(5):
            if call == user[i][j]:
                user[i][j] = 0

    if check_bingo(user):
        print(turn)
        break
