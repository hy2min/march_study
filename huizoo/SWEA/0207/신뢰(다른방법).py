T = int(input())
for tc in range(1, T+1) : 
    arr = input().split()
    N = int(arr[0])
    order = [(arr[i],int(arr[i+1])) for i in range(1, 2*N, 2)]

    robots = {
        'O' : {'loc' : 1, 'time' : 0},
        'B' : {'loc' : 1, 'time' : 0},
    }

    total_time = 0

    for robot, button in order : 
        # 현재 로봇의 상태
        loc = robots[robot]['loc']
        last_time = robots[robot]['time']

        # 이동 거리 = 눌러야하는 버튼 위치 - 현재 위치
        move = abs(button - robots[robot]['loc'])
        
        # 이전 동작 이후 대기한 시간(=미리 이동한 시간)
        stay = total_time - last_time

        # 바로 버튼을 누를 수 있거나 부족한 이동시간 만큼 더 이동해야 함
        additional_move = max(0, move-stay)

        # 0 혹은 부족한 이동거리만큼 더한 이후 버튼 누르는 시간 1초 추가
        total_time += additional_move + 1

        # 현재 상태 갱신
        robots[robot]['loc'] = button
        robots[robot]['time'] = total_time
    
    print(f'#{tc} {total_time}')