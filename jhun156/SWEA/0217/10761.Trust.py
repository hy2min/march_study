'''
tc 입력
문자열입력
1. B 가 눌러야 하는 버튼 따로
   O가 눌러야 하는 버튼 따로 저장
Time=0  -> answer가 될것임
2.


if B가 먼저 이동을 한다면
         B가 버튼누르는데 걸리는 시간 구한 후 Time에 더하고
         그 사이에
         O가 누를 버튼이 있다면
                     O가 다음버튼누르는데 걸리는시간 < B버튼 누른데 걸리는시간
                               O를 다음 버튼에 위치 시키고
                      O가 다음버튼 누르는데 걸리는 시간 > B버튼 누르는데 걸리는시간
                                O가 우측으로 이동해야 한다면
                                       O위치 + B이동시간
                                O가 좌측으로 이동해야 한다면
                                       O 위치 - B이동시간
else (O가 먼저 이동해야 한다면)
       위에 적었던 설계 반대로 적기

'''
'''
testcase = int(input())
for tc in range(1, testcase + 1):
    ans = 0
    test = input().split() # 수행 명령어 입력
    N = int(test[0]) # 명령의 개수
    Blue = [] # 블루 버튼 위치 저장할 리스트
    Orange = [] #오렌지 버튼 위치 저장할 리스트
    for i in range(1, len(test), 2): # 4 B 2 O 1 O 2 B 4
        if test[i] == 'B':
            Blue.append(int(test[i + 1]))   # [2 4]
        else:
            Orange.append(int(test[i + 1])) # [1 2]

    nowB, nowO = 1, 1 # 현재 위치
    time = 0 # 걸리는 총 시간

    for i in range(1, len(test), 2):
        if test[i] == 'B':          # 4 B 2 O 1 O 2 B 4
            bt_location = Blue.pop(0)
            Bmove = abs(bt_location - nowB) + 1
            time += Bmove
            nowB = bt_location


            if len(Orange) != 0:
                bt_location = Orange[0]
                if Bmove > abs(bt_location - nowO):
                    nowO = bt_location
                else:
                    if nowO < bt_location:
                        nowO += Bmove
                    else:
                        nowO -= Bmove


        else:
            bt_location = Orange.pop(0)
            Omove = abs(bt_location - nowO) + 1
            time += Omove
            nowO = bt_location

            if len(Blue) != 0:
                bt_location = Blue[0]
                if Omove > abs(bt_location - nowB):
                    nowB = bt_location
                else:
                    if nowB < bt_location:
                        nowB += Omove
                    else:
                        nowB -= Omove

    print(f'#{tc} {time}')
'''
import sys
sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    arr = list(input().split())
    N = int(arr[0])
    B_lst = []
    O_lst = []
    ans = 0
    B,O = 1,1
    next = 0
    for i in range(1,len(arr),2):
        if arr[i] == 'B':
            B_lst.append(arr[i+1])
        else:
            O_lst.append(arr[i+1])

    for i in range(1,len(arr),2):
        if arr[i] == 'B':
            next = B_lst.pop(0)
            B_move = abs(B-next) + 1
            ans += B_move
            B = next






































