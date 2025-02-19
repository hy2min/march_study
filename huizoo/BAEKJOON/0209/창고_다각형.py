N = int(input())# 기둥 개수
arr = [0]*1001  # 기둥의 높이들을 담을 배열 생성
s = 0           # 다각형 넓이 초기화
cnt = 0         # 기둥 개수(while문 반복 조건에 들어감)
for _ in range(N) : 
    i, h = map(int, input().split())
    arr[i] = h  # 인덱스i에 높이 저장
# 양 옆 0 제거(배열 크기 줄이기 위함)
start = next(i for i in range(1001) if arr[i] > 0) 
end = next(i for i in range(1000, -1, -1) if arr[i] > 0)
arr = arr[start:end+1]

reversed_arr = arr[::-1]
max_arr = max(arr)

# 처음 최대 높이가 여러개일 때
if arr.count(max_arr) >= 2 : 
    # 첫번째 등장 하는 위치 저장
    max_index1 = arr.index(max_arr)
    # 마지막 위치 저장
    max_index2 = len(arr) - reversed_arr.index(max_arr) - 1 
    # 넓이 저장
    s = max_arr*(abs(max_index1 - max_index2) + 1)
    # 기둥개수 카운트
    for i in arr[max_index1:max_index2+1] : 
        if i : cnt += 1  
# 처음 최대 높이가 1개 일때
else : 
    max_index1 = arr.index(max_arr) # 첫번째랑 마지막 인덱스 동일
    max_index2 = arr.index(max_arr)
    s += max_arr
    cnt += 1

def Carculate_left(lst) :   # 받은 리스트의 우측에서 좌측으로 탐색
        global s, cnt
        if not lst :        # 비어있다면 비어있는 리스트 반환
            return []
        length = len(lst)   # 창고 바닥 길이
        height = max(lst)   # 제일 높은 기둥 높이
        max_index = lst.index(height)   # 제일 높은 기둥의 인덱스
        s += height*(length-max_index)  # 넓이 저장
        for i in lst[max_index:] :  # 그 사이 기둥 개수 카운트
            if i : cnt += 1    

        else :
            # 제일 높은 기둥의 인덱스보돠 좌측의 리스트만 반환
            return lst[:max_index]  
        

def Carculate_right(lst) :  # 받은 리스트의 좌측부터 우측으로 탐색
        global s, cnt
        if not lst : 
            return []
        length = len(lst)
        height = max(lst)
        max_index = lst.index(height)
        s += height*(max_index+1)
        for i in lst[:max_index+1] : 
            if i : cnt += 1
        if max_index + 1 == length : 
            return []
        else :     
            return lst[max_index+1:]

arr2 = arr[:max_index1]     # 제일 높은 기둥 기준 좌측에 있는 리스트
arr3 = arr[max_index2+1:]   # 제일 높은 기둥 기준 우측에 있는 리스트
while cnt < N : # 기둥 개수 전부 카운트하면 종료
    # 좌측 리스트가 비어있지 않다면 실행
    if arr2 : 
    # 좌측 탐색하고 넓이 계산한 만큼 지운 리스트를 다시 좌측 리스트에 할당
        arr2 = Carculate_left(arr2)
    if arr3 : 
        arr3 = Carculate_right(arr3)
    # 만약 둘다 비어있다면 탈출
    if not arr2 and not arr3:
        break

print(s)