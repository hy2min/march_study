T = int(input())
for tc in range(1, T+1):
    data = input().split()
    N = int(data[0])
    # 명령 시퀀스를 (로봇, 목표버튼) 튜플의 리스트로 생성
    seq = [(data[i], int(data[i+1])) for i in range(1, 2 * N, 2)]
    
    # 각 로봇의 상태를 하나의 딕셔너리로 관리:
    # 'pos' : 현재 위치, 'time': 마지막으로 버튼을 누른 시각(available 시간)
    robots = {
        'O': {'pos': 1, 'time': 0},
        'B': {'pos': 1, 'time': 0}
    }
    
    current_time = 0  # 전체 소요 시간
    
    # 각 명령을 순차적으로 처리
    for robot, target in seq:
        # 해당 로봇의 현재 상태를 불러옴
        pos = robots[robot]['pos']
        last_time = robots[robot]['time']
        
        # 로봇이 목표까지 이동해야 하는 시간(거리)
        travel_time = abs(target - pos)
        # 로봇이 이전 동작 이후로 대기한 시간(즉, 이미 미리 이동한 시간)
        idle_time = current_time - last_time
        # 부족한 이동 시간만큼 기다려야 함 (idle_time이 travel_time보다 작을 경우)
        wait = max(0, travel_time - idle_time)
        # 버튼을 누르는 1초와 추가 대기(wait)시간을 포함하여 총 소요 시간 갱신
        current_time += wait + 1
        # 해당 로봇의 현재 위치와 마지막 동작 시각 갱신
        robots[robot]['pos'] = target
        robots[robot]['time'] = current_time

    print(f"#{tc} {current_time}")
