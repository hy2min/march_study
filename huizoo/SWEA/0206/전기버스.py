t = int(input())
for tc in range(1, t+1) : 
    K, N, M = map(int, input().split())
    bus = list(map(int, input().split()))
    bus.insert(0, 0)    # 출발점(정류장 0번) 추가
    bus.append(N)   # 종점 추가
    n = 0   # 이동한 거리 계산
    i = 0   # 정류장 번호 카운트
    charge_cnt = 0  # 충전 횟수 카운트
    flag = False    # 설치가 잘못된 경우 판별

    '''
    반복조건 :
    i < M+2 : 정류장 번호가 오버되면 종료
    n + K < N : 이동한거리(n)와 이동가능한 거리(K)를 더했을 때 더이상 충전하지 않고 종점(N)에 도달 가능할 때 종료
    '''
    while i < M+2 and n+K < N : 
        move = 0    # 이동한 거리 n에 더해줄 값 초기화
        for j in range(1, M+2-i) : # 정류장 i번 이후를 탐색, M+2-i의 최대값은 1
            if j == 1 :     # 첫 정거장부터 도착을 못하면 이후 계산 필요 없이 0 출력
                if bus[i+j]-bus[i] > K : # 정류장 0번을 기준으로 1번까지의 거리가 K보다 길면 
                    flag = True
                    break
                else : 
                    move = bus[i+j]-bus[i] # 정거장 사이 거리 할당
                    temp = j    # 이동한 정거장 수 임시저장
            elif bus[i+j]-bus[i] > K : # 정거장 사이거리가 K보다 길면 
                break
            else : 
                move = bus[i+j]-bus[i] # 정거장 사이 거리 할당
                temp = j    # 이동한 정거장 수 임시저장
        n += move   # for문 다 돌고 이동한 정거장 사이 거리 n에 증가
        i += temp   # for문 다 돌고 이동한 정거장 수 i에 증가 -> 다음 while문은 새롭게 도착한 정거장 기준으로 시작
        charge_cnt += 1 # 도착하면 충전
        if flag :   
            break
    if flag : # 중간에 정류장 사이 거리가 길어서 이동하지 못한 경우 발생했으면 0 출력
        print(f'#{tc} 0')
    else :     
        print(f'#{tc} {charge_cnt}')