import sys
sys.stdin = open("input.txt", "r")

answer = []
T = int(input())
for tc in range(1, T+1):
    # N명, 0초부터 만들기 시작, M초의 시간을 들이면 K개의 붕어빵 제작 가능
    N, M, K = map(int, input().split())
    # 배열 길이 N
    visit = list(map(int, input().split()))
    # 해당 시간 구역에 붕어빵이 K개씩 있음(첫번째 구역은 0개)
    sector = 11112 // M
    made = [K]*(sector+1)
    made[0] = 0

    flag = 0
    for time in visit:
        sector2 = time // M
        for i in range(sector2, -1, -1):
            if i == 0:
                flag = 1
                break
            if made[i] == 0:
                continue
            else:
                made[i] -= 1
                break
        if flag:
            break

    if flag:
        answer.append(f'#{tc} Impossible')
    else:
        answer.append(f'#{tc} Possible')

print('\n'.join(answer))
