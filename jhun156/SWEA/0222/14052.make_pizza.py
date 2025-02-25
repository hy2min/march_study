# import sys
# sys.stdin = open("input.txt","r")
from collections import deque

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    q = deque()         # 피자의 치즈양 추적
    index_q = deque()   # 현재 피자의 arr에서의 원래 인덱스, //2 의 특성상 나중에 인덱스 추적이 어려울수 있기때문에
    for i in range(N):  # 치즈양과 인덱스 번호 queue 2개를 꾸준히 추적하며 답 찾기
        q.append(arr[i])
        index_q.append(arr.index(arr[i]))
    tmp = N     # 회전을 돌며 추가할 피자의 시작 인덱스
    ans = 0     # 나중에 답이 될 것

    while q:

        now = q.popleft()   # 치즈양 관찰
        now_index = index_q.popleft()   # 현재 피자의 arr상 인덱스
        arr[now_index] //= 2    # 기본 반복 틀, arr의 값을 수정해가며 추적
        now //= 2
        if now == 0:        # 피자 치즈양이 0이 되면 탈출
            while tmp < M:          # 더이상 추가할 피자가 없으면 while문 동작 x
                q.append(arr[tmp])
                index_q.append(tmp)
                tmp += 1
                break
        else:
            q.append(now)
            index_q.append(now_index)

        if len(index_q) == 1:       # 마지막 피자만 남았을 경우
            ans = index_q.popleft()
            break

    ans += 1        # 피자번호는 1번부터 시작하기 때문
    print(f"#{tc} {ans}")


