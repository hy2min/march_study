T = int(input())
for tc in range(1, T+1):
    N, *arr = input().split()
    N = int(N)
    loc_O, loc_B, t = 1, 1, 0
    for i in range(1, 2 * N, 2):
        arr[i] = int(arr[i])
    
    while arr:  # 배열에 요소가 남아있는 동안 반복
        temp_t = 0
        # 각 로봇의 첫 등장 인덱스 저장
        if 'O' in arr:
            index_O = arr.index('O')
        if 'B' in arr:
            index_B = arr.index('B')
        robot = arr[0]  # 이번에 움직일 로봇
        button = arr[1] # 누를 버튼의 위치
        
        if 'O' in arr and 'B' in arr:   # 두 로봇이 모두 남아있을 때
            if robot == 'O':    # O가 버튼을 누를 차례라면
                temp_t += abs(button - loc_O)   # 이동거리만큼 시간 추가
                loc_O = button                  # O는 목표 버튼까지 이동
                temp_t += 1                     # 버튼 누르는 데 1초 소요
                # 동시에, B는 temp_t 시간 동안 다음 목표 방향으로 이동
                next_target = arr[index_B+1]                    # B 목표 버튼 설정
                if next_target >= loc_B:                        # 목표 버튼 도달하기 직전 혹은 도달했을 때
                    loc_B = min(loc_B + temp_t, next_target)    # B는 O가 이동한 거리만큼 전진하다가 목표 버튼을 만난다면 그 자리에 멈춰야 하기 때문에 min값으로 할당
                else:                                           # 목표 버튼이 뒤에 있다면
                    loc_B = max(loc_B - temp_t, next_target)    # O가 이동한 거리만큼 후진하다가 목표 버튼을 만난다면 그 자리에 멈춰야 하기 때문에 max값으로 할당
                        
            elif robot == 'B':  # B가 버튼을 누를 차례라면
                temp_t += abs(button - loc_B)
                loc_B = button
                temp_t += 1
                next_target = arr[index_O+1]
                if next_target >= loc_O:
                    loc_O = min(loc_O + temp_t, next_target)
                else:
                    loc_O = max(loc_O - temp_t, next_target)
                        
        elif 'B' in arr:    # B만 남았을 때
            temp_t += abs(button - loc_B) + 1
            loc_B = button
        else:               # O만 남았을 때
            temp_t += abs(button - loc_O) + 1
            loc_O = button
        
        if len(arr) > 2:
            arr = arr[2:]
        else:
            arr = []
        t += temp_t
        
    print(f'#{tc} {t}')
