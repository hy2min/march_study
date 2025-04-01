# Dijkstra 그래프 최소비용 구하기
name = 'ABCDE'
inf = int(21e7)
arr = [[0, 3, inf, 9, 5],
       [inf, 0, 7, inf, 1],
       [inf, inf, 0, 1, inf],
       [inf, inf, inf, 0, inf],
       [inf, inf, 1, inf, 0],]

used = [0]*5
used[0] = 1 # A(0번 인덱스)를 시작점으로 등록
result = [0, 3, inf, 9, 5] # 첫번째 경유지를 시작점인 A로 놓았을 경우

def select_ky():
    Min = int(21e8)
    Minindex = 0
    for i in range(5):
        if used[i] == 0 and result[i] < Min:
            Min = result[i]
            Minindex = i
    return Minindex

def dijkstra():
    # 경유지 선택
    for i in range(4):
        via = select_ky()
        used[via] = 1

    # 시작 -> 경유
    # 시작 -> 경유 -> 도착 비교 후 작은 값으로 갱신
        for j in range(5): # result 배열에 갱신할 것임
            baro = result[j]
            kyoung = result[via] + arr[via][j]
            if baro > kyoung:
                result[i]=kyoung






dijkstra