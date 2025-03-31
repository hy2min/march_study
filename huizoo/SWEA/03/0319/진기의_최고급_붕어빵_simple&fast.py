import sys
sys.stdin = open("input.txt", "r")

answer = []
T = int(input())
for tc in range(1, T+1):
    # N명, 0초부터 만들기 시작, M초의 시간을 들이면 K개의 붕어빵 제작 가능
    N, M, K = map(int, input().split())
    # 배열 길이 N
    visit = sorted(list(map(int, input().split())))
    # cnt : 사람 수
    cnt = 0
    flag = 0
    for time in visit:
        # 사람이 방문한 시간에 남아있는 붕어빵 수가 0개 이하라면
        if K*(time//M) - cnt <= 0:
            flag = 1
            break
        else:
            cnt += 1

    if flag:
        answer.append(f'#{tc} Impossible')
    else:
        answer.append(f'#{tc} Possible')

print('\n'.join(answer))